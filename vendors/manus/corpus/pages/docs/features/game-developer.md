> ## Documentation Index
> Fetch the complete documentation index at: https://manus.im/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Game Developer

> Create browser games from a playable template and a plain-language description. Edit gameplay, art, and sound in the Edit panel, host online multiplayer games on a Cloud Computer, and publish a link so others can play.

## What it is

**Game Developer** (Game Dev) lets you create games that run in a web browser. You start from a playable template, such as a scrolling, jumping, or block-puzzle game. You describe the gameplay, the world, and the visual style in everyday language. Manus then creates a first version that you can play in the same session. You do not need any coding experience.

After the first version is ready, you shape the game with direct controls or by asking Manus for changes. This page uses three terms:

| Term | What it means |
| :- | :- |
| **Edit panel** | The panel next to the conversation, with the **Preview**, **Assets**, **Code**, **Multiplayer**, and **Dashboard** tabs. You use it to watch the game, manage assets, adjust code, and change movement, art, and scenes. |
| **Tweak panel** | A settings panel inside the game. You use it to change values such as speed, gravity, damage, and spawn rate while you play. |
| **Cloud Computer** | A dedicated environment that you purchase. For an online multiplayer game, it is the server that runs the game. It stays on when your laptop is closed. |

Game Dev is a Manus Studio add-on and is part of Manus 2.0.

## How to use it

The video below shows the full workflow: a first prompt, the tweak panel, an AI asset edit, and an online multiplayer lobby.

[Manus Game Developer overview](https://www.youtube.com/embed/oEgZUBVXRLY)

### Start a new game

**1. Open Game development**

On the Manus home screen, select **Game development** ("Turn your idea into a game").

![The Manus home screen with the Game development shortcut highlighted above the Build and Create cards](https://mintcdn.com/docs-manus/DVkEJwKy4lDs5bIO/images/game-dev/home-game-development.webp?fit=max\&auto=format\&n=DVkEJwKy4lDs5bIO\&q=85\&s=b82f9e1bcd26d842cd0fd95e5f46553c)

You can also select **Build**, then select **Game development**.

![The Build menu above the Manus input box, with Game development in the bottom-right card](https://mintcdn.com/docs-manus/DVkEJwKy4lDs5bIO/images/game-dev/build-menu.webp?fit=max\&auto=format\&n=DVkEJwKy4lDs5bIO\&q=85\&s=a36c217d0841dc4517d59faf1ad9be1e)

**2. Choose a playable template**

Start your project from a playable template that is close to your idea, such as a scrolling, jumping, or block-puzzle game. (unverified: the full list of templates and where they appear.)

**3. Describe your game**

Write what the player does, how the player wins, and how the game looks. A **Create Games** tag shows in the input box. See the example prompts below.

![A detailed game prompt in the Manus input box with the Create Games tag selected](https://mintcdn.com/docs-manus/DVkEJwKy4lDs5bIO/images/game-dev/first-prompt.webp?fit=max\&auto=format\&n=DVkEJwKy4lDs5bIO\&q=85\&s=58ebb230c37be09dda229b945de12bad)

**4. Send your prompt**

Select the send button. If you are not signed in, Manus asks you to sign in first.

**5. Play the first version**

When Manus finishes, play the game in the **Preview** tab of the Edit panel. Note what you want to change before you continue.

**Example prompts**

A short prompt is enough to start:

```text theme={null}
A bright platformer where you jump between islands and collect stars.
```

A detailed prompt gives Manus more to work with. This prompt is from the video above:

```text theme={null}
Create a Super Mario World-style side-scroller with a branching 3-level world map,
secret exits and unlockable paths. Include running, cape gliding, a rideable
companion, and keys for hidden routes. Use a claymation floating-cloud-island art style.
Add an Edit Panel to tweak gameplay parameters in real time.
```

### Start from a showcase game

1. Go to the [Game Dev page](https://manus.im/features/game-dev) and scroll to **Explore games**.
2. Open a showcase game and play it.
3. Choose to build on it. Manus adds the game to the input box.
4. Describe the changes you want, for example a new theme, new characters, or different rules.
5. Send your prompt. Sign in if Manus asks you to.

### Work in the Edit panel

The Edit panel opens next to the conversation. You can make a change by hand in the panel, or ask Manus to take another pass on the same project.

![The Edit panel with the Assets tab open, showing backgrounds and characters, asset details, and an Ask Manus to edit button](https://mintcdn.com/docs-manus/DVkEJwKy4lDs5bIO/images/game-dev/edit-panel-assets.webp?fit=max\&auto=format\&n=DVkEJwKy4lDs5bIO\&q=85\&s=a7d6e388db4ca074519a3a26162b7647)

| Tab | What you do there |
| :- | :- |
| **Preview** | Play the game and watch it in motion. |
| **Assets** | Browse, edit, and replace images, audio, and fonts. |
| **Code** | View and adjust the game code, if you want to. |
| **Multiplayer** | Set up a server so that other people can join the game online. |
| **Dashboard** | (unverified: what this tab shows.) |

When you change one part of the game, the rest stays as it was. For example, if one character's hair should be silver instead of brown, select that character and change it. You do not need to restart the game.

To reopen the Edit panel later, select **Manage** on the game card in the conversation. (unverified: that **Manage** opens the Edit panel.)

### Adjust gameplay with the tweak panel

Manus creates a tweak panel for each game. The panel lists settings that belong to that game, so the settings differ from game to game. A game can use a different name for it, such as "Tuning panel".

![A tuning panel with sliders for run speed, jump power, player gravity, enemy count, camera zoom, and other settings](https://mintcdn.com/docs-manus/DVkEJwKy4lDs5bIO/images/game-dev/tweak-panel.webp?fit=max\&auto=format\&n=DVkEJwKy4lDs5bIO\&q=85\&s=2e12529c4d2181942384524bcae09edf)

1. Start playing your game in the **Preview** tab.
2. Open the tweak panel. In the game shown above, a **Tweak** button and the **F1** key open the panel. Your game can use a different button or key.
3. Move a slider, for example run speed, jump power, player gravity, enemy count, or camera zoom.
4. Keep playing to feel the effect of the change.
5. Select **Save & Resume** to keep testing with the new values, or select **Reset defaults** to go back to the original values.
6. When you like the result, ask Manus to apply the values to your game. For example: "Apply my current tweak panel values as the new defaults."

> [!NOTE]
>
> The tweak panel saves your values as a local draft. It does not change the game's default values. The values become part of your game only after you ask Manus to apply them.

If your game has no tweak panel, or a setting you need is missing, ask Manus to add it:

```text theme={null}
Add a tweak panel so I can adjust gameplay settings in real time.
```

```text theme={null}
Add a slider for enemy spawn rate to the tweak panel.
```

### Change characters, art, and sound

Assets are the characters, backgrounds, items, images, audio, and fonts in your game.

**Edit an asset with AI**

1. In the Edit panel, open the **Assets** tab.
2. Filter by type, for example **Characters** or **Backgrounds**, or search for the asset by name.
3. Select the asset. Its details show on the right.
4. In the text box, describe the change. For example: "Transform the fire beetle into a wind beetle."
5. Select **Ask Manus to edit**.
6. Play the game again in the **Preview** tab to check the new asset in context.

The video shows the same kind of edit from the asset grid, with a **Send to Manus** button:

![A grid of game assets with one enemy selected and a prompt box with a Send to Manus button](https://mintcdn.com/docs-manus/DVkEJwKy4lDs5bIO/images/game-dev/asset-edit.webp?fit=max\&auto=format\&n=DVkEJwKy4lDs5bIO\&q=85\&s=e8e953827b6bbbb76e7580ef6aca5d17)

**Use your own images or sounds**

1. In the input box, select **+** and attach your image or sound files.
2. Tell Manus how to use each file. For example: "Use the attached drawing as the main character. Use the attached sound when the player collects a coin."
3. Play the game to check that the new assets look and sound right.

You can also ask for asset changes in plain language, without files. For example: "Replace the hero with a fox in a red scarf, in the same art style."

### Play, test, and improve your game

1. Play through your game from the start.
2. Write down what feels wrong, such as a jump that is too short or a level that is too hard.
3. Tell Manus about one or two changes at a time, in the same conversation.
4. Play the new version and repeat.

Use the table below to phrase common requests:

| What you notice | What to ask Manus |
| :- | :- |
| The game is too hard or too easy | "Make level 1 easier: fewer enemies and wider platforms." |
| The controls feel wrong | "Let the player hold Shift to run, and make the jump more responsive." |
| Players do not know what to do | "Show the controls at the bottom of the screen and add short hints for new abilities." |
| The game feels short | "Add two more levels and a world map that connects them." |
| The look is not right | "Change the art style to pixel art with a sunset color palette." |
| Players need their own settings | "Add an in-game settings menu with music volume, sound effects volume, and a reduced motion option." |

### Add multiplayer to your game

You do not need a server to build a game. Whether you need one for multiplayer depends on where the players are:

| Multiplayer type | Example | Server needed? |
| :- | :- | :- |
| **Local multiplayer** | Two players share one screen, or play split screen on one device. | No |
| **Online multiplayer** | Players join from their own devices, with an invite link or a room code. | Yes, a Cloud Computer |

**Add local multiplayer**

1. Ask Manus for a local mode. For example: "Add a two-player split-screen mode. Player 1 uses WASD and player 2 uses the arrow keys."
2. Play the game in the **Preview** tab with a second player on the same device.

**Set up online multiplayer**

An online game needs a server that stays on and that every player can reach. In Game Dev, a Cloud Computer is that server. Manus configures it for you. You do not need to set up your own server or networking.

1. Ask Manus for online multiplayer features. For example: "Make this an online racing game where friends join a room with an invite link or a room code."
2. In the Edit panel, open the **Multiplayer** tab.
3. Select **Cloud Computer**. If you do not have one yet, buy one.
4. Wait while Manus sets up the game on the Cloud Computer.
5. Open the game, create a room, and share it with friends. In the game shown below, the lobby has **Copy invite link** and **Join by room code** options.

![An online race lobby with a room code, a player list, and options to copy an invite link or join by room code](https://mintcdn.com/docs-manus/DVkEJwKy4lDs5bIO/images/game-dev/multiplayer-lobby.webp?fit=max\&auto=format\&n=DVkEJwKy4lDs5bIO\&q=85\&s=f62cf9c5675d5d27668dfe5132320fb0)

You can also create a Cloud Computer in your settings. Open **My computers**, then under **Cloud computers**, select **Create now**.

![The My computers settings page with a Create now button under Cloud computers](https://mintcdn.com/docs-manus/DVkEJwKy4lDs5bIO/images/game-dev/cloud-computer.webp?fit=max\&auto=format\&n=DVkEJwKy4lDs5bIO\&q=85\&s=4e82c71cf434a88dbb024050d47d3af7)

> [!NOTE]
>
> A Cloud Computer is a separate purchase. (unverified: the price.)

> [!WARNING]
>
> Use one Cloud Computer for each online game. Running more than one game on the same Cloud Computer is not recommended. The current hardware is not optimized for multiple game instances and session ports on one server.

### Publish and share your game

You can publish in two ways:

| Method | How it works |
| :- | :- |
| **When Manus prompts you** | When your game is ready, Manus asks if you want to publish it. Confirm to publish. |
| **Manually** | In the Edit panel, select the publish button in the top-right corner. The button shows **Published** when the game is live. |

After you publish:

1. Copy the link to your published game. The link also shows on the game card in the conversation.
2. Send the link to the people you want to play. They play in their web browser.
3. Collect feedback, then ask Manus for changes in the same conversation.

The Game Dev page also states that you can prepare launch materials for your game with Manus. (unverified: what these materials include.)

## What you need to know

* **Game Dev is a Manus Studio add-on.** (unverified: which plans include it and how users get access.)
* **Every game starts from a playable template.** Templates include scrolling, jumping, and block-puzzle games. You can play the first version in the first session.
* **Games run in a web browser.** Supported genres include platformers, puzzles, and racing games. The video also shows a side-scroller, a kart racer, a split-screen snowboarding game, a physics puzzle game, and a mini-golf game.
* **Changes are targeted.** When you change one character, scene, or setting, the rest of the game stays as it was.
* **Tweak panel values are a local draft.** They do not change your game until you ask Manus to apply them. Other players do not see your draft values.
* **The tweak panel is specific to each game.** Manus chooses the settings based on your game. If a setting is missing, ask Manus to add it.
* **You do not need a server to build a game.** Single-player games and local multiplayer games, such as split screen or same screen, run without one.
* **Online multiplayer needs a Cloud Computer.** The Cloud Computer is the server behind your game. It is a separate purchase, and it stays on when your laptop is closed.
* **Host one online game per Cloud Computer.** Running several games on one Cloud Computer is not recommended with the current hardware.
* **You must sign in to send a prompt.** You can browse and play showcase games first.
* **Your edits stay in one conversation.** Keep working on a game in the same conversation so that Manus keeps the full context.
* **Games can show a "Made with Manus" label.** The games in the video show this label in the corner of the screen. (unverified: whether the label appears on all published games and whether you can remove it.)
* **Credits.** Manus uses a credit-based system, and credit use depends on the complexity of the task. See [Plans and Pricing](https://manus.im/docs/introduction/plans.md). (unverified: the typical credit cost of a game.)
* **No game engine is named.** The sources do not state which engine or technology Manus uses. (unverified: whether you can export a game to another engine or to an app store.)
* **The feature is still changing.** Manus states that Manus 2.0 has rough edges and will continue to improve. Some steps on this page can change.

## Tips

* **Pick the closest template.** A template that already matches your game type gives you a better first version.
* **Start with three facts.** Tell Manus what the player does, how the player wins, and how the game looks. Add details in later messages.
* **Start small.** Ask for one level or one game mode first. Add levels, modes, and multiplayer after the core game feels right.
* **Make one change at a time.** Short, specific requests make it easier to see what changed and to undo a change you do not like.
* **Edit by hand when you know exactly what to change.** Use the **Assets** tab or the tweak panel for one specific item. Ask Manus for new rules, levels, and menus.
* **Lock in tuned values before you publish.** Ask Manus to apply your tweak panel values. Otherwise, players get the original defaults.
* **Describe what you see and what you expect.** For example: "When I land on a moving platform, the player slides off. The player should move with the platform."
* **Name a familiar style.** References such as "claymation", "pixel art", or "low-poly 3D" help Manus match the look you want.
* **Try local multiplayer first.** A split-screen or same-screen mode needs no server. Add online play when you want friends to join from their own devices.
* **Test online multiplayer with more than one window or device.** Join your own room from a second browser window to check the invite flow before you share it.

## FAQ

> [accordion] Can I use a showcase game as a starting point?
>
> Yes. Open a showcase on the [Game Dev page](https://manus.im/features/game-dev), play it, and choose to build on it. Manus adds the game to the input box, where you describe your changes.

> [accordion] What is the Edit panel?
>
> The Edit panel is the panel next to the conversation. In it, you can watch the game in motion, manage assets, adjust code, and change movement, art, and scenes by hand.

> [accordion] Can I change one character without resetting the game?
>
> Yes. Select that character and change it. The rest of the game stays as it was.

> [accordion] Can I use my own images, characters, or sounds?
>
> Yes. Attach your files in the input box and tell Manus how to use each one in the game.

> [accordion] The game does not do what I asked. What should I do?
>
> Send a short, specific message. Describe what happens now, what you expect instead, and where in the game it happens. Ask for one change at a time, then play the game again to check it.

> [accordion] I changed values in the tweak panel, but the published game did not change. Why?
>
> The tweak panel saves your values as a local draft. Ask Manus to apply your approved values to the game. Then publish again if needed.

> [accordion] Do I need a server to build a game?
>
> No. You need a server only for online multiplayer. Single-player games and local multiplayer games, such as split screen or same screen, do not need one.

> [accordion] How do I make a multiplayer game?
>
> For local multiplayer, ask Manus for a split-screen or same-screen mode. For online multiplayer, ask Manus for online features. Then, in the Edit panel, open the **Multiplayer** tab, select **Cloud Computer**, and buy one if you do not have one. Manus handles the rest.

> [accordion] Can a Cloud Computer host a game server?
>
> Yes. For a Game Dev project, the Cloud Computer is the server behind your game. It stays on when your laptop is closed.

> [accordion] Do I need to set up my own server?
>
> No. Manus configures the Cloud Computer for your game. You do not need to set up servers or networking yourself.

> [accordion] Can one Cloud Computer host more than one game?
>
> It is not recommended. The current Cloud Computer hardware is not optimized for multiple game instances and session ports on one server. Use one Cloud Computer for each online game.

> [accordion] How many players can join a multiplayer game?
>
> The racing game in the video shows a room for up to 8 players. (unverified: the maximum number of players for each game type.)

> [accordion] How do I publish my game?
>
> Manus prompts you to publish when your game is ready. You can also publish manually with the publish button in the top-right corner of the Edit panel.

> [accordion] How do other people play my game?
>
> Share the link to your published game. Other people open the link and play in their web browser. In online multiplayer games, friends can also join your room with an invite link or a room code.

> [accordion] If I change my game after I publish it, do players see the change?
>
> (unverified: whether the published link updates automatically or whether you must publish again.)

> [accordion] How many credits does a game use?
>
> Credit use depends on the complexity of the task. See [Plans and Pricing](https://manus.im/docs/introduction/plans.md) for details. A Cloud Computer for online multiplayer is a separate purchase. (unverified: typical credit costs for Game Dev.)

## Further reading

* Launch blog: [Introducing Game Dev](https://manus.im/blog/introducing-game-developer)
* Help center: [How can I use Game Dev in Manus?](https://help.manus.im/en/articles/17190151-how-can-i-use-game-dev-in-manus)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.