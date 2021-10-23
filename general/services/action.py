from general.models.action import Action, ActionStatus, ActionVerb, ActionObjectType


def create_login_action(user):
    Action.create_action(
        actor=user,
        description='User logged in',
        token_change=0,
        status=ActionStatus.COMPLETE,
        verb=ActionVerb.LOGGED_IN,
        object_type=ActionObjectType.USER,
        object_id=user.id,
        data=None
    )


def create_logout_action(user):
    Action.create_action(
        actor=user,
        description='User logged out',
        token_change=0,
        status=ActionStatus.COMPLETE,
        verb=ActionVerb.LOGGED_OUT,
        object_type=ActionObjectType.USER,
        object_id=user.id,
        data=None
    )


def give_user_consent_action(user, data):
    Action.create_action(
        actor=user,
        description='User consented.',
        token_change=0,
        status=ActionStatus.COMPLETE,
        verb=ActionVerb.COMPLETED,
        object_type=ActionObjectType.USER,
        object_id=user.id,
        data=data
    )


def remove_user_consent_action(user, data):
    Action.create_action(
        actor=user,
        description='User removed their consent.',
        token_change=0,
        status=ActionStatus.COMPLETE,
        verb=ActionVerb.COMPLETED,
        object_type=ActionObjectType.USER,
        object_id=user.id,
        data=data
    )


def update_user_profile_action(user, data):
    Action.create_action(
        actor=user,
        description='User updated their profile.',
        token_change=0,
        status=ActionStatus.COMPLETE,
        verb=ActionVerb.UPDATED,
        object_type=ActionObjectType.USER,
        object_id=user.id,
        data=data
    )


def change_password_action(user):
    Action.create_action(
        actor=user,
        description='User changed their password.',
        token_change=0,
        status=ActionStatus.COMPLETE,
        verb=ActionVerb.UPDATED,
        object_type=ActionObjectType.USER,
        object_id=user.id,
        data=None
    )


def reset_password_email_action(user):
    Action.create_action(
        actor=user,
        description='User requested a password reset email.',
        token_change=0,
        status=ActionStatus.COMPLETE,
        verb=ActionVerb.COMPLETED,
        object_type=ActionObjectType.USER,
        object_id=user.id,
        data=None
    )


def reset_password_action(user):
    Action.create_action(
        actor=user,
        description='User reset their password.',
        token_change=0,
        status=ActionStatus.COMPLETE,
        verb=ActionVerb.UPDATED,
        object_type=ActionObjectType.USER,
        object_id=user.id,
        data=None
    )


def create_event_action(user, data):
    Action.create_action(
        actor=user,
        description='User created an event.',
        token_change=0,
        status=ActionStatus.COMPLETE,
        verb=ActionVerb.CREATED,
        object_type=ActionObjectType.USER,
        object_id=user.id,
        data=data
    )


def update_event_action(user, data):
    Action.create_action(
        actor=user,
        description='User updated an event.',
        token_change=0,
        status=ActionStatus.COMPLETE,
        verb=ActionVerb.UPDATED,
        object_type=ActionObjectType.USER,
        object_id=user.id,
        data=data
    )


def import_event_action(user, data):
    Action.create_action(
        actor=user,
        description='User imported an event.',
        token_change=0,
        status=ActionStatus.COMPLETE,
        verb=ActionVerb.DUPLICATED,
        object_type=ActionObjectType.USER,
        object_id=user.id,
        data=data
    )


def course_registration_verify_action(user):
    Action.create_action(
        actor=user,
        description='User entered verification code.',
        token_change=0,
        status=ActionStatus.COMPLETE,
        verb=ActionVerb.COMPLETED,
        object_type=ActionObjectType.USER,
        object_id=user.id,
        data=None
    )


def course_registration_student_number_action(user):
    Action.create_action(
        actor=user,
        description='User entered correct student number.',
        token_change=0,
        status=ActionStatus.COMPLETE,
        verb=ActionVerb.COMPLETED,
        object_type=ActionObjectType.USER,
        object_id=user.id,
        data=None
    )


def course_registration_confirm_name_action(user):
    Action.create_action(
        actor=user,
        description='User successfully confirmed name.',
        token_change=0,
        status=ActionStatus.COMPLETE,
        verb=ActionVerb.COMPLETED,
        object_type=ActionObjectType.USER,
        object_id=user.id,
        data=None
    )


def create_submission_action(submission):
    Action.create_action(
        actor=submission.user,
        description="User submitted a solution",
        token_change=0,
        status=ActionStatus.COMPLETE,
        verb=ActionVerb.SUBMITTED,
        object_type=ActionObjectType.SUBMISSION,
        object_id=submission.id,
        data={
            'answer': submission.answer,
        }
    )


def create_submission_evaluation_action(submission):
    Action.create_action(
        actor=submission.user,
        description="Submission was evaluated",
        token_change=submission.tokens_received,
        status=ActionStatus.COMPLETE,
        verb=ActionVerb.EVALUATED,
        object_type=ActionObjectType.SUBMISSION,
        object_id=submission.id,
        data={
            'answer': submission.answer,
            'grade': submission.grade,
            'is_correct': submission.is_correct,
            'is_partially_correct': submission.is_partially_correct,
            'status': submission.status,
        }
    )
