> ## Documentation Index
> Fetch the complete documentation index at: https://manus.im/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Video Editor

> Make and edit videos on a multi-track timeline in Manus Studio. Start from an idea or your own footage, then refine the cut by hand or by asking Manus.

## What it is

**Video Editor** is a timeline editor in **Manus Studio**, the Manus desktop app for macOS and Windows. You describe a video or add your own footage, and Manus builds a first cut on the timeline. You then refine that cut by hand, by asking Manus in chat, or both.

<video controls playsInline src="https://mintcdn.com/docs-manus/Wy1hTsVGFOliHgSA/videos/video-editor-launch.mp4?fit=max&auto=format&n=Wy1hTsVGFOliHgSA&q=85&s=ff4d0b2344364bd4eb41bc6678458191" />

Video Editor with Alchemy mode: one prompt becomes a finished, editable video.

Each element of the video sits on its own **track**. Tracks hold video clips, images, captions, text, motion graphics, voiceover, music, and sound effects. You do not get a single flattened file. You can change one part of the video without regenerating the rest.

Video Editor also has **Alchemy mode**. In Alchemy mode, Manus acts as the creative director. It writes the script, draws the storyboard, generates the shots, scores the music, and edits the final cut from one prompt. Use Alchemy mode when quality matters most.

Video Editor works best for short product ads (30 to 60 seconds), AI UGC (user-generated-content style) videos, data motion graphics, tutorials, vlogs, and motion-led videos. You do not need video editing experience.

## How to use it

### Create a video from a description

**1. Start a video task**

Open Manus Studio or Manus on the web. Click **Create**, then select **Video**.

**2. Describe the video**

Describe the video in one or two sentences. Include the topic, the audience, the platform, the aspect ratio, the target length, and the language.

**3. Send the task**

Send the task. Manus plans the video and creates the parts it needs, such as shots, images, music, voiceover, and sound effects. Then it assembles a first cut.

**4. Review the first cut**

In Manus Studio, the first cut opens on the Video Editor timeline. If you started on the web, follow [Move a web task to Video Editor](#move-a-web-task-to-video-editor).

Example prompt:

```text theme={null}
Make a 30-second vertical (9:16) launch video for our note-taking app, in English.
Use a clean white UI style, upbeat music, captions, and end with one call to action.
```

### Make a finished video with Alchemy mode

**1. Open the video creation screen**

Open Manus Studio. Click **Create**, then select **Video**.

**2. Turn on Alchemy mode**

Select **Alchemy** in the task input. The **Alchemy templates** list opens.

**3. Pick a template**

Pick the template that is closest to your idea. The template name appears in the task input.

**4. Set the aspect ratio**

Use the ratio button in the task input, for example **16:9**, to set the frame of your video.

**5. Describe your idea and send**

Describe your idea in one sentence, then send the task.

**6. Follow the progress**

Video Editor opens and shows each stage in the left panel: script and storyboard, shot generation, sound and music, and the final cut.

**7. Fine-tune the result**

When **Your video is ready** appears, review the video on the timeline. Edit it by hand, or type a change in the prompt box below the player.

The table shows the templates in the launch video and an example prompt for each.

| Template | Example prompt |
| :- | :- |
| **Paper Cranes** | "She bursts into a thousand paper cranes and lands somewhere new." |
| **Outfit Swap** | "Make it a silver sequin dress." |
| **Mural to Real** | "Pull the paper plane off the mural and make it land giant." |
| **Sketch → 3D Film** | "Turn my 4-panel storyboard into a 3D animated short." |
| **Motion Graphics** | "Make an animated map of our café locations." |
| **Product Ad** | "Make a 30-second ad for our travel mug that shows how it folds flat." |

### Edit your own footage

**1. Open Manus Studio**

Open Manus Studio and sign in. If you do not have the app, download it from [manus.im/desktop](https://manus.im/desktop).

**2. Add your footage**

Click **Create**, then select **Video**. Drag your clips into the chat, or tell Manus which folder on your computer contains them.

**3. Describe the edit**

State the type of video, the target length, and the aspect ratio. List any moments that must stay in the video.

**4. Send the task**

Send the task. Manus imports the clips and reviews them. It transcribes speech, samples frames, and selects the strongest moments.

**5. Review the first cut**

Manus places the first cut on the Video Editor timeline. Refine it by hand or by asking Manus, as described below.

> [!NOTE]
>
> Manus can only read folders that you connect in **My Computer**. If Manus cannot find your footage, see [Desktop](https://manus.im/docs/features/desktop.md) for how to connect a folder.

Use the prompts below as a starting point. Replace the details with your own.

| Use case | Example prompt |
| :- | :- |
| **Talking-head highlight** | "Cut this interview into a 60-second vertical short. Open with the strongest point, remove pauses and repetition, and add accurate captions." |
| **Vlog** | "Turn these travel clips into a 3-minute vlog with an opening, the best moments, and a natural ending. Keep the ambient sound and add light music." |
| **Promotional ad** | "Make a 20-second ad from these product photos and clips. Show the main benefit, add narration and captions, and end with a call to action." |
| **Step-by-step tutorial** | "Turn this screen recording into a how-to video. Show each step in order, label each step, and add narration." |
| **Software demo** | "Use these screen recordings to show how our export feature solves a real user problem. Emphasize the cursor and add captions." |
| **Event recap** | "Make a 90-second highlight reel from this meetup footage. Include the venue, key moments, and attendee reactions." |
| **Long video to short clips** | "Turn this meeting recording into three short clips for social media, each under 45 seconds." |

### Move a web task to Video Editor

**1. Click Edit in Video Editor**

In a finished video task on the web, click **Edit in Video Editor**.

**2. Install Manus Studio if prompted**

If you do not have Manus Studio, Manus guides you to download it. Install the app and sign in with the same account.

**3. Open the same task**

Open the same task in Manus Studio. The video opens on the Video Editor timeline.

### Edit on the timeline by hand

Use your mouse to make changes directly on the timeline. You can preview the sequence at any time.

| To do this | What you can change |
| :- | :- |
| **Adjust pacing** | Trim clips, rearrange scenes, and change the timing of each clip. |
| **Change text** | Add titles and text, rewrite captions, and change their style and position. |
| **Adjust sound** | Work with voiceover, music, and audio clips, and set the volume of each. |
| **Change the frame** | Resize the canvas, for example to 9:16 for vertical video or 16:9 for widescreen. |
| **Add your own media** | Bring your own video, images, or audio into the project next to the assets Manus generated. |

### Edit by asking Manus

**1. Describe the change**

In the same task, tell Manus what to change. For example: "Turn the music down," "Tighten the middle section," or "Replace the product shot with my photo."

**2. Let Manus update the project**

Manus edits the same project that you see on the timeline. It continues from your latest manual edits and does not start over.

**3. Check the result**

Review the change on the timeline. Adjust it by hand if you need a more precise result. If you prefer an earlier result, see [Open an earlier version](#open-an-earlier-version).

### Open an earlier version

Each version of your video opens in its own tab at the top of the workspace. Earlier versions stay available as you keep editing.

**1. Find the version tabs**

Look at the tab bar at the top of the workspace. Each video version has its own tab. The tab shows the file name of that version, for example `bricklane_launch_v8` or `bricklane_launch_v9`.

**2. Open a version**

Click a tab to open that version. The header shows its file name and the time it was last modified.

**3. Compare versions**

Play the video, then switch between tabs to compare versions.

**4. Continue from an earlier version**

To build on an earlier version, tell Manus its file name and ask it to continue from that version (unverified).

![Manus Studio workspace with three video version tabs at the top. The active tab plays a vertical reel, and the header shows its file name and last-modified time.](https://mintcdn.com/docs-manus/Wy1hTsVGFOliHgSA/images/video-editor-version-tabs.webp?fit=max\&auto=format\&n=Wy1hTsVGFOliHgSA\&q=85\&s=7d50679fbcb0a799e1891f14152a88fa)

Each version opens in its own tab. In this example, the tabs show two versions of a launch video and a vertical reel.

### Export your video as an MP4

**1. Find the video file**

In the task chat, find the card for the video file. The card shows the file name, the type **Video**, and the file size. Each version has its own card. If you do not see the card, click **View all files in this task**.

**2. Download the MP4**

Hover over the video file card, then click the download icon on the right side of the card. The video downloads as an MP4 file.

**3. Publish the video**

Upload the MP4 file to the platform where you publish, such as YouTube, TikTok, Instagram, or X.

![Manus Studio task chat with a video file card that shows a download icon on hover. The Video Editor tab on the right plays the same video.](https://mintcdn.com/docs-manus/Wy1hTsVGFOliHgSA/images/video-editor-export-file.webp?fit=max\&auto=format\&n=Wy1hTsVGFOliHgSA\&q=85\&s=8727f96bf81fbcf69a8c069b49f49ca8)

Hover over the video file card in the task chat, then click the download icon.

***

## What you need to know

### Where Video Editor runs

* **Manus Studio for the full editor:** Timeline editing and Alchemy mode run in Manus Studio for macOS (Apple Silicon) and Windows.
* **Web for a quick start:** On the web, you can start a video and review the first version. To edit it on the timeline, open the task in Manus Studio.
* **Local files give the best results:** For the best results, use footage that is stored on your computer and work in Manus Studio.

### Plans and credits

* **All plans:** Video Editor is available on every plan, including the free plan. Video generation can be limited on some plans.
* **Credits:** Making and editing videos with Manus uses credits. Paid plans add more credits every month. See [Plans and Pricing](https://manus.im/docs/introduction/plans.md) for details.

### How edits work

* **One shared project:** Manual edits and chat edits change the same project. When you ask Manus for a change after you edit by hand, Manus continues from your version.
* **Separate tracks:** Each clip, image, caption, text effect, music cue, and sound effect stays on its own track. You can change one element without affecting the others.
* **Previous versions:** Each version of your video opens in its own tab at the top of the workspace. If an edit does not work, click the tab of an earlier version.
* **Mixed sources:** One project can combine your own footage, generated video clips, images, and visuals that Manus makes with code.

### Formats and processing

* **Aspect ratios:** You can make vertical videos (9:16) for Reels, TikTok, and Shorts, widescreen videos (16:9), and other formats for UGC and social posts. You can also resize the canvas on the timeline.
* **Input types:** You can add video clips, images, audio, screenshots, and screen recordings. The supported file formats and maximum file sizes are not listed yet (unverified).
* **Export format:** Video Editor exports MP4 files. More export options are planned.
* **Processing time:** Processing time depends on the length of your footage and the complexity of the video.

### Accuracy

* **Review facts and captions:** For videos that use web research, Manus may flag facts that it could not confirm. Check those facts, names, and captions before you publish.
* **First cuts can run long:** The first cut can be longer than your target. Ask Manus to cut it to the length you need.

***

## Tips

* **Use Alchemy mode for high-stakes videos.** For launch films, ads, and other videos where quality matters most, start in Alchemy mode.
* **Give the key details in your first prompt.** State the platform, aspect ratio, target length, language, and tone. This reduces the number of changes you need later.
* **List the moments that must stay.** Name the clips, quotes, or shots that Manus must keep in the final video.
* **Use the timeline for precise changes.** Instructions such as "move this half a second earlier" are hard to state in chat. Make these changes by hand.
* **Use chat for broad changes.** Ask Manus to change the pacing, the mood, the music, or the structure of the whole video.
* **Ask for a segment list before you cut.** Ask Manus to list each segment with its length and spoken lines. Then decide which segments to remove.
* **Lower the music under speech.** Ask Manus to dim the music whenever someone speaks.
* **Share a reference video.** Give Manus a link to a video with the pacing or style you want. Manus can study it and make its own version.
* **Replace generated assets with your own.** Swap a generated image for your real product photo or logo on the timeline.
* **Keep brand materials in a Project.** Store logos, brand guidelines, and past scripts in a [Project](https://manus.im/docs/features/projects.md) so that each video task starts with the same context.
* **Make several clips from one recording.** Ask Manus to turn one long interview or meeting into multiple short clips.

***

## FAQ

> [accordion] Do I need video editing experience?
>
> No. Describe the video in your own words, and Manus makes the first version. Open the timeline only when you want to change details yourself.

> [accordion] What is the difference between Alchemy mode and a standard video task?
>
> In a standard video task, Manus makes the video that you describe. In Alchemy mode, Manus also takes on the creative direction: script, storyboard, shots, music, and edit. Use Alchemy mode when quality matters most. You can edit the result on the timeline in both cases.

> [accordion] Can I use Video Editor in my browser?
>
> You can start a video and review the first version in Manus on the web. To edit on the timeline or use Alchemy mode, open the task in Manus Studio.

> [accordion] Why does Edit in Video Editor ask me to download an app?
>
> Video Editor runs in Manus Studio, the Manus desktop app. If the app is not installed, Manus guides you to download it. After you install it, open the same task in the app.

> [accordion] Can I use Video Editor on the free plan?
>
> Yes. Video Editor is available on every plan, including the free plan. Video generation can be limited on some plans. See [Plans and Pricing](https://manus.im/docs/introduction/plans.md).

> [accordion] Will asking Manus for a change undo my manual edits?
>
> No. Manual edits and chat edits change the same project. Manus continues from your latest version and does not regenerate the whole video.

> [accordion] Can I go back to an earlier version?
>
> Yes. Each version opens in its own tab at the top of the workspace. Click a tab to open that version. See [Open an earlier version](#open-an-earlier-version).

> [accordion] The first cut is longer than I want. What should I do?
>
> Tell Manus the target length, for example "Cut this to 60 seconds." You can also ask Manus to list each segment with its length first, then choose what to remove.

> [accordion] Manus cannot find my footage. What should I do?
>
> Drag the clips directly into the chat. If you refer to a folder, give its full path, and make sure that the folder is connected in **My Computer**. See [Desktop](https://manus.im/docs/features/desktop.md).

> [accordion] Can I make vertical videos for YouTube Shorts, TikTok, and Reels?
>
> Yes. Ask for a 9:16 frame in your prompt, or resize the canvas on the timeline. You can also make widescreen videos and other formats for UGC and social posts.

> [accordion] Can I combine my own footage with AI-generated clips?
>
> Yes. You can add your own media and generated assets to the same project. Each one stays on its own track.

> [accordion] Which export formats are available?
>
> Video Editor exports MP4 files. More export options are planned. To download a video, hover over its file card in the task chat and click the download icon.

***

## Further reading

* [Introducing Video Editor in Manus 2.0](https://manus.im/blog/introducing-video-editor)
* [Introducing Manus 2.0](https://manus.im/blog/introducing-manus-2-0), which introduces Manus Studio and Alchemy mode


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.