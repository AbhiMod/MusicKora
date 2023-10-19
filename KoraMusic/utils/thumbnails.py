

import os
import re
import textwrap
import random
import aiofiles
import aiohttp
from PIL import (Image, ImageDraw, ImageEnhance, ImageFilter,
                 ImageFont, ImageOps)
from youtubesearchpython.__future__ import VideosSearch

from KoraMusic import app
from config import MUSIC_BOT_NAME

YOUTUBE_IMG_URL = [ 
"https://graph.org/file/7ca0ae3fe2e327d3dcc86.jpg",
"https://te.legra.ph/file/e7629907cf40431ec6ccd.jpg",
"https://graph.org/file/a39f6f364c34e724ef367.jpg",
"https://graph.org/file/88fcdd5e044279c0d1747.jpg",
"https://graph.org/file/fcc2837e0f83cd4d08765.jpg",
"https://graph.org/file/1fcd0f7d5fdb7e700dca5.jpg",
"https://graph.org/file/39c27bf76bf8742a148c4.jpg",
"https://graph.org/file/2c5e6f38ca28687c8c3e8.jpg",
"https://graph.org/file/71682c8fb277c84031c0f.jpg",
"https://graph.org/file/c118207cef395ceb196ee.jpg",
"https://graph.org/file/1b765cd3d9fcc99614a32.jpg",
"https://graph.org/file/d935b6fbb2e3936b1850a.jpg",
"https://graph.org/file/e94c4566b9a7cf7d23a4b.jpg",
"https://graph.org/file/fd2196561ba6e8c4c46a9.jpg",
"https://graph.org/file/17cbf7cedbc44b85c7bda.jpg",
"https://graph.org/file/cd72a1c4c3b1d52070a90.jpg",
"https://graph.org/file/8663d4f19f5d9c30f8ff9.jpg",
"https://graph.org/file/255e5501d4f8b2e348d87.jpg",
"https://graph.org/file/cf28d171b08e0590749c7.jpg",
"https://graph.org/file/a1d7ccd85d58b076f8f88.jpg",
"https://graph.org/file/aa10da451e1e263105516.jpg",
"https://graph.org/file/cba9cd9f3fd1bcf841db2.jpg",
"https://graph.org/file/a06eaee8e9070840947bd.jpg",
"https://graph.org/file/83f5a1123580bd75f591e.jpg",
"https://graph.org/file/2f4f60ba8405368505ba2.jpg",
"https://graph.org/file/18da6db0b032a6c428471.jpg",
"https://graph.org/file/cd0f7fd0dc68ce8dbe2d4.jpg",
"https://graph.org/file/eabfa2836ec2e6fb41cd5.jpg",
"https://graph.org/file/59fb7cd9ea2d1331e75ef.jpg",
"https://graph.org/file/748e908aaa6cbb6c03402.jpg",
"https://graph.org/file/a26d09d472ddce5532ca2.jpg",
"https://graph.org/file/3fb4577387c3934eed027.jpg",
"https://graph.org/file/e19ab57b45fe4c9765869.jpg",
"https://graph.org/file/4b9b5d7b6e1a46c55dea1.jpg",
"https://graph.org/file/d7f9dd74e37f3e4985075.jpg",
"https://graph.org/file/8fd58648581a8f8d3f19b.jpg",
"https://te.legra.ph/file/7b10f2f5ffb1bc6075197.jpg",
"https://te.legra.ph/file/628180b161e5233889919.jpg",
"https://te.legra.ph/file/e8571aeadbd3204a28076.jpg",
"https://te.legra.ph/file/8d3944528638ff176d115.jpg",
"https://te.legra.ph/file/95c760593b889ac2cf283.jpg",
"https://te.legra.ph/file/76df768a14abb189597d1.jpg",
"https://graph.org/file/e22c45fd3484101750e55.jpg",
"https://graph.org/file/a950d4ce51c144d86ed23.jpg",
"https://graph.org/file/ef9a008b504798372f1f5.jpg",
"https://graph.org/file/dd589ba59d9fcf46d3642.jpg",
"https://graph.org/file/9cec2e206055333a8e5db.jpg",
"https://graph.org/file/3d6a1d301fc1eed2fb68a.jpg",
"https://graph.org/file/9160ced720578a0e37a56.jpg",
"https://graph.org/file/e4765f28baa44cfa216fc.jpg",
"https://graph.org/file/772e967e6a9f3592f1d5a.jpg",
"https://graph.org/file/95b52b5defbd4ea34bc9a.jpg",
"https://graph.org/file/94ca673ba4947804e4302.jpg",
"https://graph.org/file/91a098df46d7344579581.jpg",
"https://graph.org/file/125446c45cf48a07f3ee5.jpg",
"https://graph.org/file/82a12bb7d42253f8fc52f.jpg",
"https://graph.org/file/ca8448d171ed891c1a5f0.jpg",
"https://graph.org/file/f74432342c46fd825ae06.jpg",
"https://graph.org/file/8b23fc09c5498f5f9261b.jpg",
"https://graph.org/file/3b36e5407c3ab7fe92e17.jpg",
"https://graph.org/file/00f5e1d09f1cf1049bf78.jpg",
"https://graph.org/file/6d0d387a63c154c5cf79b.jpg",
"https://graph.org/file/e1dd0fa5c594119f724ef.jpg",
"https://graph.org/file/d2001bbfbd878c217cc91.jpg",
"https://graph.org/file/14e306381330584aa8b7e.jpg",
"https://graph.org/file/bf4926a4d314a50987c56.jpg",
"https://graph.org/file/671d080b083562a0566d9.jpg",
"https://graph.org/file/2fe342162983f4c8a6c99.jpg",
"https://graph.org/file/bdb6fce1f958a72b5cad9.jpg",
"https://graph.org/file/1324a281e310c1036e936.jpg",
"https://graph.org/file/9cec2e206055333a8e5db.jpg",
"https://graph.org/file/c07707bc36710271d9d11.jpg",
"https://graph.org/file/ff37901868715173a130a.jpg",
"https://graph.org/file/def0b8e3a0e556d4616d0.jpg",
"https://graph.org/file/d5d907baa5370f3c16184.jpg",
"https://graph.org/file/adca2dcea5c3fcb9c2336.jpg",
"https://graph.org/file/d7d8c5e7f52dbfd9f4b61.jpg",
"https://graph.org/file/fa4ac129a63e9d5079404.jpg",
"https://graph.org/file/5ec4f598005322fddc96f.jpg",
"https://graph.org/file/3c2ad196eae8d2114b0ae.jpg",
"https://graph.org/file/1f97423211d30f18b1b8a.jpg",
"https://graph.org/file/0f9edb65806f4364ec1c7.jpg",
"https://graph.org/file/71cb5858ace52c4238344.jpg",
"https://graph.org/file/9ded63e3bdb576fe4137e.jpg",
"https://graph.org/file/36cd3fa37ae80f3cd74c8.jpg",
"https://graph.org/file/f6103d075c94c9677bd9d.jpg", 
"https://telegra.ph/file/32b773adce82bfdf80aee.jpg",
"https://telegra.ph/file/aec018719d49566471512.jpg",
"https://telegra.ph/file/d67754ccf1f3e134606d5.jpg",
"https://telegra.ph/file/85dd8099b114b70b58380.jpg",
"https://telegra.ph/file/fbbc941a30c3fdf995b08.jpg",
"https://telegra.ph/file/6f7fdc142293fed0a0d17.jpg",
"https://telegra.ph/file/fb31622c76cb524109ff1.jpg",
    ]


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def gen_thumb(videoid):
    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

            async with aiohttp.ClientSession() as session:
                async with session.get(thumbnail) as resp:
                    if resp.status == 200:
                        f = await aiofiles.open(
                            f"cache/thumb{videoid}.png", mode="wb"
                        )
                        await f.write(await resp.read())
                        await f.close()

            youtube = Image.open(f"cache/thumb{videoid}.png")
            image1 = changeImageSize(1280, 720, youtube)
            image2 = image1.convert("RGBA")
            background = image2.filter(filter=ImageFilter.BoxBlur(30))
            enhancer = ImageEnhance.Brightness(background)
            background = enhancer.enhance(0.6)
            Xcenter = youtube.width / 2
            Ycenter = youtube.height / 2
            x1 = Xcenter - 250
            y1 = Ycenter - 250
            x2 = Xcenter + 250
            y2 = Ycenter + 250
            logo = youtube.crop((x1, y1, x2, y2))
            logo.thumbnail((520, 520), Image.ANTIALIAS)
            logo = ImageOps.expand(logo, border=15, fill="white")
            background.paste(logo, (50, 100))
            draw = ImageDraw.Draw(background)
            font = ImageFont.truetype("assets/font2.ttf", 40)
            font2 = ImageFont.truetype("assets/font2.ttf", 70)
            arial = ImageFont.truetype("assets/font2.ttf", 30)
            name_font = ImageFont.truetype("assets/font.ttf", 30)
            para = textwrap.wrap(title, width=32)
            j = 0
            draw.text(
                (5, 5), f"{MUSIC_BOT_NAME}", fill="white", font=name_font
            )
            draw.text(
                (600, 150),
                "NOW PLAYING",
                fill="white",
                stroke_width=2,
                stroke_fill="white",
                font=font2,
            )
            for line in para:
                if j == 1:
                    j += 1
                    draw.text(
                        (600, 340),
                        f"{line}",
                        fill="white",
                        stroke_width=1,
                        stroke_fill="white",
                        font=font,
                    )
                if j == 0:
                    j += 1
                    draw.text(
                        (600, 280),
                        f"{line}",
                        fill="white",
                        stroke_width=1,
                        stroke_fill="white",
                        font=font,
                    )

            draw.text(
                (600, 450),
                f"Views : {views[:23]}",
                (255, 255, 255),
                font=arial,
            )
            draw.text(
                (600, 500),
                f"Duration : {duration[:23]} Mins",
                (255, 255, 255),
                font=arial,
            )
            draw.text(
                (600, 550),
                f"Channel : {channel}",
                (255, 255, 255),
                font=arial,
            )
            try:
                os.remove(f"cache/thumb{videoid}.png")
            except:
                pass
            background.save(f"cache/{videoid}.png")
            return f"cache/{videoid}.png"
    except Exception as e:
        print(e)
        return random.choice(YOUTUBE_IMG_URL)
