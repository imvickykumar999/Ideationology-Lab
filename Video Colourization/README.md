
# `Video_colorization`.[py](https://github.com/imvickykumar999/Video-Colorization/blob/main/video_colorization.py)

    pip install -r requirements.txt

-----------------

## `Uploaded` [`PlayList`](https://www.youtube.com/playlist?list=PLyeWzbpbicN032fYAmjBoxPQn9AlB1uwl)

- [Beqaraar Karake Hamen Yun Na Jaaiye](https://youtu.be/r4cJrr0WczE) **(32.4k+ views)**
- [Mera Joota Hai Japani](https://www.youtube.com/shorts/FlktPZTxCq4)
- [Haal Kaisa Hai Janaab Ka](https://youtu.be/dRTmhoUrr_0) **(7.4k+ views)**
- [Itna Na Mujhse Tu Pyaar Badha](https://www.youtube.com/watch?v=AFy573PU8Og)
- [Aa chal ke tujhe main leke chaloon](https://www.youtube.com/watch?v=gqDkgqpBrwo)

--------------------------------

## `Transformed Video`

https://user-images.githubusercontent.com/50515418/208450925-81a28039-1ee6-48e6-afc4-e41ebb9ab95c.mp4

### `It took 20 minutes to transform only 10 seconds video.`

## `Original Video`

https://user-images.githubusercontent.com/50515418/208451041-b5ab039c-36d4-432f-9047-f15d3da0bea9.mp4

----------------------

**Clone the repository; install dependencies**

```
gh repo clone imvickykumar999/Video-Colorization
pip install requirements.txt
```

**Colorize!** This script will colorize an image. The results should match the images in the `imgs_out` folder.

```
python demo_release.py -i imgs/output.jpg
```

**Model loading in Python** The following loads pretrained colorizers. See [demo_release.py](https://github.com/imvickykumar999/Video-Colorization/blob/main/extras/demo_release.py) for some details on how to run the model. There are some pre and post-processing steps: convert to Lab space, resize to 256x256, colorize, and concatenate to the original full resolution, and convert to RGB.

```python
import colorizers
colorizer_eccv16 = colorizers.eccv16().eval()
colorizer_siggraph17 = colorizers.siggraph17().eval()
```

--------------------

### Original implementation (Caffe branch)

https://pub.towardsai.net/colorizing-images-with-deep-learning-a34d11587643

The original implementation contained train and testing, our network and AlexNet (for representation learning tests), as well as representation learning tests. It is in Caffe and is no longer supported. Please see the [caffe](https://github.com/richzhang/colorization/tree/caffe) branch for it.

### Citation ###

If you find these models useful for your resesarch, please cite with these bibtexs.

```
@inproceedings{zhang2016colorful,
  title={Colorful Image Colorization},
  author={Zhang, Richard and Isola, Phillip and Efros, Alexei A},
  booktitle={ECCV},
  year={2016}
}

@article{zhang2017real,
  title={Real-Time User-Guided Image Colorization with Learned Deep Priors},
  author={Zhang, Richard and Zhu, Jun-Yan and Isola, Phillip and Geng, Xinyang and Lin, Angela S and Yu, Tianhe and Efros, Alexei A},
  journal={ACM Transactions on Graphics (TOG)},
  volume={9},
  number={4},
  year={2017},
  publisher={ACM}
}
```

----------------------------------

## `Input command` in [Curl Commands Online](https://reqbin.com/curl)

    curl \
        -F 'image=https://keyassets.timeincuk.net/inspirewp/live/wp-content/uploads/sites/12/2019/01/BW-using-curves.jpg' \
        -H 'api-key:c34c7088-11a1-456b-9a77-1384500eb46f' \
        https://api.deepai.org/api/colorizer 
    
-----------------------

## `Output Response` : [deepai.org](https://deepai.org/machine-learning-model/colorizer) need payment of 5 doller per month.
`I avoid such websites which need payments, this repository can do same for free.`

    {
        "status": "Out of API credits - please enter payment info in your dashboard: https://deepai.org/dashboard"
    }
    
---------------------------

## `Output Video` on : [YouTube](https://youtube.com/shorts/FlktPZTxCq4?feature=share)

![image](https://user-images.githubusercontent.com/50515418/208730165-93c8807d-8cf7-4626-827d-eaf191b71e06.png)
