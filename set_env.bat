REM Enable Microsoft Foundry integration
set CLAUDE_CODE_USE_FOUNDRY=1

REM Azure resource name (replace {resource} with your resource name)
REM ANTHROPIC_FOUNDRY_RESOURCE=dce-ai-foundry-project-1
REM Or provide the full base URL:
set ANTHROPIC_FOUNDRY_BASE_URL=https://<AI-Foundry-Resource>.openai.azure.com/anthropic

REM Set models to your resource's deployment names
set ANTHROPIC_DEFAULT_SONNET_MODEL=claude-haiku-4-5
set ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5
set ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-5

