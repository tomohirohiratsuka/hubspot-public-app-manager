import argparse
import fire

from commands.card_command import CardCommand
from commands.timeline_command import TimelineCommand
from commands.workflow_command import WorkflowCommand
from config.settings import Config


def main():
	"""
	Main entry point for the CLI.
	:return:
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'-e',
		'--env',
		help='Environment to load the correct .env file',
		choices=['local', 'staging', 'production'],
		default=None
	)
	args, remaining_argv = parser.parse_known_args()

	config = Config(env=args.env)
	workflow_command = WorkflowCommand(config)
	card_command = CardCommand(config)
	timeline_command = TimelineCommand(config)

	if remaining_argv:
		fire.Fire({
			'workflow': workflow_command,
			'card': card_command,
			'timeline': timeline_command,
		}, command=remaining_argv)
	else:
		fire.Fire(workflow_command)


if __name__ == '__main__':
	main()
