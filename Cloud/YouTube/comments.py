
api_key = 'AIzaSyC3EsHgVkGg11WfvEgVYuamubsGsjq1n-I'
# api_key = 'AIzaSyCcJX4qdbo9caqxZSKDmuBjNVWfvq8_Wcs'

from googleapiclient.discovery import build

# creating youtube resource object
youtube = build('youtube', 'v3',
                developerKey=api_key)

def yts(q = 'puppies', maxResults = 10):
    dogs_videos_ids = youtube.search().list(
        part="id",
        type='video',
        regionCode="US",
        order="relevance",
        q=q,
        maxResults=maxResults,
        fields="items(id(videoId))",
    ).execute()

    return dogs_videos_ids


def com(video_id = 'Cpc_rHf1U6g'):

    dict = {}
    # empty list for storing reply
    replies = []

    video_response=youtube.commentThreads().list(
    part='snippet,replies',
    videoId=video_id
    ).execute()

    for item in video_response['items']:

        # Extracting comments
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']

        # counting number of reply of comment
        replycount = item['snippet']['totalReplyCount']

        # if reply is there
        if replycount>0:

            # iterate through all reply
            for reply in item['replies']['comments']:

                # Extract reply
                reply = reply['snippet']['textDisplay']

                # Store reply is list
                replies.append(reply)

        # print comment with list of reply
        # print(comment, replies, end = '\n\n')
        dict.update({comment: replies})

        # empty reply list
        replies = []
    return dict


# https://www.thepythoncode.com/article/using-youtube-api-in-python

def tvl(video_id = 'hlznpxNGFGQ'):

    video_request=youtube.videos().list(
        part='snippet,statistics',
        id=video_id
    )

    video_response = video_request.execute()
    title = video_response['items'][0]['snippet']['title']
    likes = int(video_response['items'][0]['statistics']['likeCount'])
    views = int(video_response['items'][0]['statistics']['viewCount'])
    publishedAt = video_response['items'][0]['snippet']['publishedAt']
    publishedAt = publishedAt.split('T')[0]
    print('********************', publishedAt)

    return title, f'{likes:,}', f'{views:,}', publishedAt
