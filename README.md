# Setup

## Install Claude Code 

Standard steps

## Set up Claude Code Proxy 

git clone https://github.com/fuergaosi233/claude-code-proxy.git

cd claude-code-proxy

pip install -r requirements.txt

copy .env.example .env

Set variable values

### To run with Azure OpenAI

Set following vars, comment out ANTHROPIC_API_KEY and OPENAI_BASE_URL on top of the file

OPENAI_API_KEY=""
OPENAI_BASE_URL="https://<your-resource-name>.openai.azure.com"
AZURE_API_VERSION="2025-01-01-preview"
BIG_MODEL="gpt-4o"
MIDDLE_MODEL="gpt-4o"
SMALL_MODEL="gpt-4o"

# Run 

## Run the proxy server

python start_proxy.py

## Run Claude Code 


set ANTHROPIC_BASE_URL=http://localhost:8082

DO NOT set ANTHROPIC_API_KEY

To disable posting Telemetry event (the proxy does not support an endpint for doing this, so unless these vars are set, it will keep on showing an error on the proxy console e.g. "POST /v1/messages?beta=true HTTP/1.1" 404 Not Found): 

set CLAUDE_CODE_DISABLE_TELEMETRY=true
set CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=true
set OTEL_SDK_DISABLED=true

With above set, Run Claude Code:   

>> cd  <project_fodlr>
>> claude

Now Claude Code will connect to local proxy server, and will NOT try to login to Claude account.

# Use Claude Code

## Sample Prompt to create the game

I want to build a Python game for my 12-year-old son who loves Pokémon. Let's build a text-based RPG called 'Terminal Monsters'.

Requirements:

Monster System: Create a Monster class with HP, Level, and a Type (Fire, Water, Grass).

Type Advantages: Implement a multiplier where Water does 2x damage to Fire, etc.

The 'Catch' Mechanic: Instead of Pokéballs, the player uses 'Patches' to fix the glitches.

ASCII Art: Use Python to print cool ASCII art borders and simple monsters.

Save System: Use a JSON file so he can save his progress and level up his monsters over time.

The Twist: Every time a monster levels up, ask it to generate a 'Special Move' name based on a random tech word (e.g., 'Firewall Blast' or 'Overclock Tackle').

Start by creating the core engine in a file called game.py


