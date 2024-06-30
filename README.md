# About this
This is a repository for managing the hubspot public app while development.

# Pre-requisite
```terminal
poerty install
```

# Configuration
You should make environment files for each environment.
```terminal
cp .env.example .env.{ENV}
```

# Structure
```terminal
.
├── README.md
├── actions
│   ├── base_action.py
│   └── example_send_message_action.py
├── cards
│   ├── base_card.py
│   └── example_card.py
├── commands
│   ├── __init__.py
│   ├── card_command.py
│   ├── timeline_command.py
│   └── workflow_command.py
├── config
│   └── settings.py
├── exceptions
│   ├── action_not_found_error.py
│   ├── card_not_found_error.py
│   └── timeline_not_found_error.py
├── main.py
├── poetry.lock
├── pyproject.toml
└── timelines
    ├── base_timeline.py
    └── example_timeline.py
```

# Workflow Commands Basics
```terminal
python main.py -e {ENV} {COMMAND_TARGET} {COMMAND} {COMMAND_ARGS}
```
`COMMAND_TARGET` is `workflow` or `card` or `timeline` custom target defined under commands directory.

# Examples

## Define public app's custom workflow action from template
```terminal
python main.py -e {ENV} workflow create {ACTION_NAME}
```

## List public app's custom workflow actions
```terminal
python main.py -e {ENV} workflow list
```

## Delete public app's custom workflow action
```terminal
python main.py -e {ENV} workflow delete {DEFINITION_ID}
```

## Find public app's custom workflow action
```terminal
python main.py -e {ENV} workflow find {DEFINITION_ID}
```

## Update public app's custom workflow action
```terminal
python main.py -e {ENV} workflow update {DEFINITION_ID} {ACTION_NAME}
```

# Note
## Debugging
On local environment, you can not use `localhost` to debug.
So you should configure [webhook.site](https://webhook.site/) to debug.

## Time lag
It takes time to reflect the changes in the public app, especially the labels.
So you should wait for a while to see the changes.