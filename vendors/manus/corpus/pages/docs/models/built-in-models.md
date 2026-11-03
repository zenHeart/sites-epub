> ## Documentation Index
> Fetch the complete documentation index at: https://manus.im/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Built-in Models

> The video, image, audio, and 3D models built into Manus, what each one is for, and how to choose one. All built-in models use Manus credits.

## What it is

Manus includes video, image, audio, and 3D models. These are **built-in models**. You use them in any Manus task, and they use your Manus credits. You do not need an account or API key with the model provider.

By default, Manus picks a model for each request. You can also choose a model yourself.

> [!NOTE]
>
> Built-in models are different from [Manus Flex](https://manus.im/docs/models/manus-flex.md). Flex connects your own API key for the language model that runs the agent. Built-in models generate media and do not use your API key.

## Models in Manus

### Video

* **Seedance 2.5** (ByteDance): Make 4 to 30 second videos with sound, guided by up to 30 reference images.
* **Seedance 2.0** (ByteDance): Make 4 to 15 second videos in up to 1080p, with a Fast option.
* **Veo 3.1** (Google): Make 4, 6, or 8 second clips, in 1080p at 8 seconds.
* **Gemini Omni Flash** (Google): Edit a video you already have, or make a new 3 to 10 second clip.
* **MiniMax H3** (MiniMax): Make 5 to 15 second videos in 768p or 1080p.

### Image

* **GPT Image 2.5** (OpenAI): Generate and edit images, including transparent PNGs. This is the default image model.
* **Nano Banana 2.1** (Google): Create posters, comics, and infographics from a prompt.
* **Nano Banana Pro** (Google): Create detailed images for professional creative work.
* **Nano Banana 2** (Google): Create and edit images from a prompt or your own photos.

### Audio

* **Lyria 3.5** (Google): Make songs with vocals or instrumental tracks of up to about three minutes.
* **Gemini 3.8 Flash TTS** (Google): Turn a script into natural speech.
* **ElevenLabs Sound Effects v2** (ElevenLabs): Create sound effects from 0.5 to 30 seconds long, including seamless loops.

### 3D

* **Tripo P1** (Tripo): The default 3D model, for low-poly game props and characters.
* **Tripo P2** (Tripo): Quality mode 3D for main characters you can rig and animate.
* **Tripo v3.1** (Tripo): Turn a prompt or one image into a textured 3D model.

For examples and full specs, see [All Manus models](https://manus.im/models).

## How to use it

1. **Let Manus choose.** Describe what you want and send it. Manus picks a suitable model.
2. **Choose from the menu.** In **Video** or **Design**, open the model menu below the input box and select a model.
3. **Name the model.** Start your request with "Use \[model name]", for example "Use Veo 3.1". Use this for models that are not in a menu.

## What you need to know

* **Credits:** Built-in models use Manus credits. Usage depends on your plan, the model, and your settings. See [Plans and Pricing](https://manus.im/docs/introduction/plans.md).
* **With Manus Flex:** Built-in models still use Manus credits when Flex is on. Your provider bills only the language model that runs the agent.
* **Menus:** The Video menu lists all video models. The Design menu lists GPT Image 2.5 and Nano Banana 2.1. Audio and 3D have no menu, so name the model in your request.
* **Video editing:** Only Gemini Omni Flash edits a video you already have. The other video models make new videos.
* **Transparent backgrounds:** Only GPT Image 2.5 makes transparent PNGs.

## Tips

* **Not sure which model to use?** Describe your goal and ask Manus which model fits.
* **Keep a product or character consistent.** Attach a reference image to your video or 3D request.
* **Refine videos on a timeline.** Open a generated video in the Video Editor in Manus Desktop.

## FAQ

> [accordion] Do I have to choose a model?
>
> No. Manus picks a model for each request. Choose one only when you need a specific capability.

> [accordion] Can I use my own API key for these models?
>
> No. Built-in models run on Manus credits. To use your own API key for the agent's language model, see [Manus Flex](https://manus.im/docs/models/manus-flex.md).

> [accordion] What happens if I ask for an older model version?
>
> Manus uses the current version. For example, a request for GPT Image 2 uses GPT Image 2.5.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.