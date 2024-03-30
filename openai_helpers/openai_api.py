import os
import openai
import urllib.request
from datetime import datetime
import sys
from argparse import ArgumentParser


class OpenaiAPI:
    def __init__(self, api_key=os.getenv("OPENAI_API_KEY")):
        openai.api_key = api_key

    def get_image(
            self,
            prompt,
            size="1792x1024",
            quality="hd",
            style="vivid",
            user=None,
            n=1,
            model="dall-e-3",
    ):
        # setting quality to hd and style to vivid based on testing
        response = openai.images.generate(
            model=model,
            prompt=prompt,
            size=size,
            quality=quality,
            style=style,
            n=n,
            user=user,
        )
        image_url = response.data[0].url
        print(f"{model} Image: {image_url}")
        return image_url

    def save_image(self, image_resp, prompt, fpath):
        fprompt = prompt.replace(" ", "_")
        # get current date and time in string format
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
        counter = 0
        for item in image_resp.data:
            fname = os.path.join(fpath, f"dalle-{dt_string}-{fprompt}-{counter}.png")
            urllib.request.urlretrieve(item.url, fname)
            counter += 1
            print(f"image saved!")

    def save_image_3(self, url, prompt, fpath):
        fprompt = prompt.replace(" ", "_")
        # get current date and time in string format
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
        fname = os.path.join(fpath, f"dalle3-{dt_string}-{fprompt}.png")
        urllib.request.urlretrieve(url, fname)
        print("image saved!")


if __name__ == "__main__":
    argparse = ArgumentParser()
    argparse.description = "Get an image from Dalle"
    argparse.add_argument(
        "-p",
        "--prompt",
        help="Prompt for Dalle. A sentence or two describing the image you want to generate and the style.",
        required=True,
    )
    argparse.add_argument(
        "-n",
        "--number",
        help="Number of images to generate. Default is 1.",
        required=False,
        default=1,
    )
    argparse.add_argument(
        "-z",
        "--size",
        help="Image size for Dalle2. Options are '256x256', '512x512', '1024x1024'. The following examples are only for Dalle3: '1024x1792', '1792x1024' (default).",
    )
    argparse.add_argument(
        "-q",
        "--quality",
        help="Image quality for Dalle3. Options are 'standard' or 'hd' (default).",
        required=False,
        default="hd",
    )
    argparse.add_argument(
        "-s",
        "--style",
        help="Image style for Dalle3. Options are 'natural' or 'vivid' (default).",
        required=False,
        default="vivid",
    )
    argparse.add_argument(
        "-u", "--user", help="User for OpenAI tracking.", required=False
    )
    argparse.add_argument(
        "-f", "--fpath", help="File path to save the file.", required=False
    )  # ,
    # default="//r7server/data/dalle/original")
    argparse.add_argument(
        "-m",
        "--model",
        help="Dalle model to use. Options are 'dall-e-3' (default) or 'dall-e-2'.",
        default="dall-e-3",
    )
    args = argparse.parse_args()
    prompt = args.prompt
    quality = args.quality
    style = args.style
    user = args.user
    fpath = args.fpath
    ai = OpenaiAPI()
    url = ai.get_image(prompt, quality=quality, style=style, user=user)
    ai.save_image_3(url, prompt, fpath)
