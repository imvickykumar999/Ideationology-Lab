# RUN on CMD : python livechatextractor.py -k AIzaSyC3EsHgVkGg11WfvEgVYuamubsGsjq1n-I -i SmO0XgU4hbY

import googleapiclient.discovery
import time
import getopt, sys

# Getting argument list. Remove 1st of them since it correspons to script name
argumentList = sys.argv[1:]

# Short options
options = "k:i:o:v:h"

# Long options
long_options = ["apikey=","videoid=", "outputfile=", "verbose=", "help"]

# Creating args dictionary to store the passed arguments
args = {opt[:-1]:None for opt in long_options[:-1]}

# ARGUMENT EXTRACTION
try:
    # Parsing arguments
    arguments, values = getopt.getopt(argumentList, options, long_options)

    # Checking each argument
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--help"):
            print("This script gets live chat messages from an ongoing " +
                  "YouTube live video and store them in a .csv file.\n")

            print("OPTIONS")

            print("-k / --apikey: (string) A valid YouTube Data API v3 key\n")

            print("-i / --videoid: (string) Id of the live video. For example, if the " +
                  "complete video's URL is: https://www.youtube.com/watch?v=N-80sVfbAno, " +
                  "then you need to set -i parameter as N-80sVfbAno " +
                  "(string assigned to 'v' URL parameter)\n")

            print("-o / --outputfile (Optional): (string) Desired name for the output file. " +
                  " If not given, the messages will be saved " +
                  "as 'results.csv'. The file will be stored in the current " +
                  "directory.")

            print("-v / --verbose: (int) Whether you want chat " +
                  "messages to be displayed on console or not (1=yes ; 0=no by default)\n\n")

            print("USAGE")

            print("python livechatgetter.py -k <API_key> -i <video_id> -o " +
                  "<output_file_name> -v <0/1>\n")
            quit()

        elif currentArgument in ('-k', "--apikey"):
            args['apikey'] = currentValue
        elif currentArgument in("-i", "--videoid"):
            args['videoid'] = currentValue
        elif currentArgument in ("-o", "--outputfile"):
            args['outputfile'] = currentValue.split('.')[0]
        elif currentArgument in ("-v", "--verbose"):
            args['verbose'] = currentValue

# In case some arg is incorrect, then raise an exception
except getopt.GetoptError as err:
    print(str(err))
    print("\nExecute <livechatgetter.py -h> for usage indications")
    quit()

# ARGUMENTS ASSESSMENT
if not args['apikey']:
    print("Error\nMissing API Key. Please, give a valid API Key with -k/--apikey argument\n")
    quit()

if not args['videoid']:
    print("Error\nMissing Video ID. Please, give a valid Video Id with -vid/--videoid argument\n")
    quit()

if not args['outputfile']:
    args['outputfile'] = 'results'


if args['verbose']:
    if args['verbose'] not in ['0', '1']:
        print("Error\nInvalid Verbose argument. Please give 0 or 1 to -vrb/--verbose argument\n")
        quit()
else:
    args['verbose'] = '1'



# Start counting execution time
start = time.time()
end = None

# API information
api_service_name = "youtube"
api_version = "v3"

# API client
youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = args['apikey'])

# Try to execute the first request in order to detect if the quota has been exceeded or if the
# API Key is valid
try:
    r = youtube.videos().list(
        part='liveStreamingDetails,snippet',
        id=args['videoid'],
        fields='items(liveStreamingDetails(activeLiveChatId),' + \
                    'snippet(title,liveBroadcastContent))'
    ).execute()

    # If request could be done, check if it contains an item; if not, then video ID is invalid
    if not r['items']:
        print("Error\nInvalid Video ID")
        quit()

except Exception as e:
    print(e)
    if "quota" in str(e):
        print("Error\nQuota exceeded. Try with another API Key")
    else:
        print("Error\nInvalid API key")
    quit()

# Checking if the retrieved video is actually a live video. Also this snippet checks
# if the video is currently streaming since it is impossible to retrieve chat messages
# from ended live videos.
args['videotitle'] = r['items'][0]['snippet'] ['title']
if r['items'][0]['snippet']['liveBroadcastContent'] != "live":
    print(f"Error\nVideo: '{args['videotitle']}' " + \
                          f"with id = {args['videoid']} is not a live video " + \
                            "or the streaming has ended.")
    quit()

# If the video is actually an ongoing live video, then check if it has the live chat activated
try:
    chatID = r['items'][0]['liveStreamingDetails']['activeLiveChatId']
except:
    print(f"Error\nLive video: '{r['items'][0]['snippet']['title']}' " + \
          f"with id = {args['videoid']} has the live chat disabled")
    quit()

# 2nd request to start up the while loop which will retrieve as much live messages as the
# quota allow, or until the stream ends.
try:
    response = youtube.liveChatMessages().list(
        liveChatId=chatID,
        part="snippet,authorDetails",
        maxResults = 1000,
        fields="nextPageToken, " + \
            "items(snippet(publishedAt, displayMessage)," + \
                    "authorDetails(channelId, displayName))"
    ).execute()

    if args['verbose'] == '0':
        print(f"Everything OK.\nLive chat messages from '{args['videotitle']}' are being obtained.\n"+
               "If you want to stop the execution before the quota is exceeded or the live "+
               "video ends, then press Ctrl+C\n\n")
except Exception as e:
    if "quota" in str(e):
        print("Error\nQuota exceeded. Messages retrieval failed to start")
    else:
        print("An unexpected error ocurred while requesting first batch of messages")
    quit()

# Dictionary where all the messages will be stored. When the retrieval ends, this object will
# be transformed into a csv file.
data = {
    'authorChannelId':[],
    'authorChannelName':[],
    'messagePublishDate':[],
    'messageContent':[]
}

# Storing first batch of messages
for item in response['items']:
    data['authorChannelId'].append(item['authorDetails']['channelId'])
    data['authorChannelName'].append(item['authorDetails']['displayName'])
    data['messagePublishDate'].append(item['snippet']['publishedAt'])
    data['messageContent'].append(item['snippet']['displayMessage'])


# Permanent loop to retrieve messages
while True:
    # In this point is common to lose the whole progress if the quota is exceeded or if the program
    # execution stops due our intervention or if the live video ends. This try/except block prevent
    # this scenarios and store all the gathered data
    try:

        # Next Token to retrieve non-duplicated messages is obtained from the previous request
        nextToken = response['nextPageToken']

        # Storing each meassage retrieved in the previous request and, if "verbose = '1'", also they
        # will be printed
        for item in response['items']:
            data['authorChannelId'].append(item['authorDetails']['channelId'])
            data['authorChannelName'].append(item['authorDetails']['displayName'])
            data['messagePublishDate'].append(item['snippet']['publishedAt'])
            data['messageContent'].append(item['snippet']['displayMessage'])

            if args['verbose'] == '1':
                print(f"{item['snippet']['publishedAt']} [{item['authorDetails']['displayName']}]: " + \
                        f"{item['snippet']['displayMessage']}")
                print("--------------------------------\n")

        # There is a mandatory wait time between requests, half second approx. But since we can retrieve
        # up to 2000 messages in just one query, then we will wait 10 seconds between requests
        # in order to save some quota usage
        time.sleep(10)

        response = youtube.liveChatMessages().list(
            liveChatId=chatID,
            part="snippet,authorDetails",
            maxResults = 1000,
            fields='nextPageToken, items(snippet(publishedAt, displayMessage),' + \
                    'authorDetails(channelId, displayName))',
            pageToken=nextToken
        ).execute()
    except:
        end = time.time()

        f = open(f"{args['outputfile']}.csv", 'w')
        f.write(",".join(list(data.keys())))
        f.write("\n")

        i = 0
        while i < len(data['authorChannelId']):
            f.write(
                f"{data['authorChannelId'][i]},"+
                f"{data['authorChannelName'][i]},"+
                f"{data['messagePublishDate'][i]},"+
                f"{data['messageContent'][i]}\n"
            )
            i += 1

        break

seconds = "{:.3f}".format(end-start)
minutes = "{:.3f}".format((end-start)/60)
hours = "{:.3f}".format((end-start)/60/60)
print(f"The program was executed by {seconds} seconds/{minutes} minutes/" +
      f"{hours} hours and {len(data['authorChannelId'])} messages were obtained.\n" +
      f"Results were saved in {args['outputfile']}.csv file.")
