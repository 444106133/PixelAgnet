# Pixel Office: Claude Code + GLM-5

This project sets up a virtual "Pixel Office" within VS Code, powered by Anthropic's **Claude Code** and Z.AI's cost-effective **GLM-5** model. As you interact with Claude Code via the terminal, the [Pixel Agents](https://marketplace.visualstudio.com/items?itemName=pablodelucca.pixel-agents) extension brings your agents to life as animated pixel characters!

## 🚀 Features

- **Cost-Effective AI:** Uses Z.AI's GLM-5 model via an Anthropic proxy, offering powerful coding assistance at a fraction of the cost of Claude integrations.
- **Multi-Agent Setup:** Includes predefined subagents (`researcher` and `coder`) to delegate tasks effectively.
- **Visual Feedback:** Watch your agents move, type, and read in real-time as they execute commands in the terminal using the Pixel Agents VS Code extension.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- **VS Code** ([Download here](https://code.visualstudio.com))
- **Node.js** (v18+) ([Download here](https://nodejs.org))
- A **Z.AI account** to get your GLM API key ([Sign up here](https://z.ai))

## 🛠️ Installation

### 1. Clone this repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/PixelAgnet.git
cd PixelAgnet
```

### 2. Install Claude Code Globally
Install the official Claude Code CLI tool via npm:
```bash
npm install -g @anthropic-ai/claude-code
```

### 3. Install Pixel Agents in VS Code
1. Open VS Code.
2. Go to the Extensions panel (`Ctrl+Shift+X` or `Cmd+Shift+X`).
3. Search for **"Pixel Agents"** by `pablodelucca` and click **Install**.

### 4. Configure Your API Key
This repository comes with the `.claude/settings.json` file pre-configured to use the GLM-5 model endpoint. You just need to add your API key:
1. Open `.claude/settings.json` in this project folder.
2. Replace `"YOUR_Z_AI_GLM_API_KEY_HERE"` with your actual Z.AI API key.

## 🎮 Usage

1. Open this project folder in **VS Code**.
2. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and run:
   ```
   Pixel Agents: Open Office View
   ```
3. Open a new terminal in VS Code (`` Ctrl+` ``).
4. Start a Claude Code session:
   ```bash
   claude
   ```
5. Give Claude a task! You can explicitly call the included subagents:
   - `@researcher find the top 5 AI trends in 2026`
   - `@coder build a clean dashboard layout in index.html`

Watch your Pixel Office activate as the characters begin walking, typing, and researching based on your prompts!

## 🐛 Troubleshooting

*   **Agents aren't moving?** Ensure you are running `claude` from within the root of this exact project folder in VS Code, as the Pixel Agents extension monitors the local `.claude/projects/` logs.
*   **Model 404 Error?** Ensure your `ANTHROPIC_BASE_URL` in `.claude/settings.json` is set precisely to `"https://api.z.ai/api/anthropic"` and not a generic paas endpoint.

---
Enjoy building with your new Pixel Office! 🚀
