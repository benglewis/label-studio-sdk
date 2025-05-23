# This file was auto-generated by Fern from our API Definition.

from label_studio_sdk import LabelStudio
from label_studio_sdk import AsyncLabelStudio
import typing
from .utilities import validate_response


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "id": 1,
        "title": "My project",
        "description": "My first project",
        "label_config": "<View>[...]</View>",
        "expert_instruction": "Label all cats",
        "show_instruction": True,
        "show_skip_button": True,
        "enable_empty_annotation": True,
        "show_annotation_history": True,
        "reveal_preannotations_interactively": True,
        "show_collab_predictions": True,
        "maximum_annotations": 1,
        "color": "color",
        "control_weights": {
            "my_bbox": {"type": "RectangleLabels", "labels": {"Car": 1, "Airplaine": 0.5}, "overall": 0.33}
        },
    }
    expected_types: typing.Any = {
        "id": "integer",
        "title": None,
        "description": None,
        "label_config": None,
        "expert_instruction": None,
        "show_instruction": None,
        "show_skip_button": None,
        "enable_empty_annotation": None,
        "show_annotation_history": None,
        "reveal_preannotations_interactively": None,
        "show_collab_predictions": None,
        "maximum_annotations": "integer",
        "color": None,
        "control_weights": ("dict", {0: (None, None)}),
    }
    response = client.projects.create()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.projects.create()
    validate_response(async_response, expected_response, expected_types)


async def test_get(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "id": 1,
        "title": "My project",
        "description": "My first project",
        "label_config": "<View>[...]</View>",
        "expert_instruction": "Label all cats",
        "show_instruction": True,
        "show_skip_button": True,
        "enable_empty_annotation": True,
        "show_annotation_history": True,
        "organization": 1,
        "prompts": [
            {
                "title": "title",
                "description": "description",
                "created_by": 1,
                "created_at": "2024-01-15T09:30:00Z",
                "updated_at": "2024-01-15T09:30:00Z",
                "organization": 1,
                "input_fields": ["input_fields"],
                "output_classes": ["output_classes"],
                "associated_projects": [1],
                "skill_name": "skill_name",
            }
        ],
        "color": "#FF0000",
        "maximum_annotations": 1,
        "annotation_limit_count": 10,
        "annotation_limit_percent": 50,
        "is_published": True,
        "model_version": "1.0.0",
        "is_draft": False,
        "created_by": {
            "id": 1,
            "first_name": "Jo",
            "last_name": "Doe",
            "email": "manager@humansignal.com",
            "avatar": "avatar",
        },
        "created_at": "2023-08-24T14:15:22Z",
        "min_annotations_to_start_training": 0,
        "start_training_on_annotation_update": True,
        "show_collab_predictions": True,
        "num_tasks_with_annotations": 10,
        "task_number": 100,
        "useful_annotation_number": 10,
        "ground_truth_number": 5,
        "skipped_annotations_number": 0,
        "total_annotations_number": 10,
        "total_predictions_number": 0,
        "sampling": "Sequential sampling",
        "show_ground_truth_first": True,
        "show_overlap_first": True,
        "overlap_cohort_percentage": 100,
        "task_data_login": "user",
        "task_data_password": "secret",
        "control_weights": {"key": "value"},
        "parsed_label_config": {"key": "value"},
        "evaluate_predictions_automatically": False,
        "config_has_control_tags": True,
        "skip_queue": "REQUEUE_FOR_ME",
        "reveal_preannotations_interactively": True,
        "pinned_at": "2023-08-24T14:15:22Z",
        "finished_task_number": 10,
        "queue_total": 10,
        "queue_done": 100,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "title": None,
        "description": None,
        "label_config": None,
        "expert_instruction": None,
        "show_instruction": None,
        "show_skip_button": None,
        "enable_empty_annotation": None,
        "show_annotation_history": None,
        "organization": "integer",
        "prompts": (
            "list",
            {
                0: {
                    "title": None,
                    "description": None,
                    "created_by": "integer",
                    "created_at": "datetime",
                    "updated_at": "datetime",
                    "organization": "integer",
                    "input_fields": ("list", {0: None}),
                    "output_classes": ("list", {0: None}),
                    "associated_projects": ("list", {0: "integer"}),
                    "skill_name": None,
                }
            },
        ),
        "color": None,
        "maximum_annotations": "integer",
        "annotation_limit_count": "integer",
        "annotation_limit_percent": None,
        "is_published": None,
        "model_version": None,
        "is_draft": None,
        "created_by": {"id": "integer", "first_name": None, "last_name": None, "email": None, "avatar": None},
        "created_at": "datetime",
        "min_annotations_to_start_training": "integer",
        "start_training_on_annotation_update": None,
        "show_collab_predictions": None,
        "num_tasks_with_annotations": "integer",
        "task_number": "integer",
        "useful_annotation_number": "integer",
        "ground_truth_number": "integer",
        "skipped_annotations_number": "integer",
        "total_annotations_number": "integer",
        "total_predictions_number": "integer",
        "sampling": None,
        "show_ground_truth_first": None,
        "show_overlap_first": None,
        "overlap_cohort_percentage": "integer",
        "task_data_login": None,
        "task_data_password": None,
        "control_weights": ("dict", {0: (None, None)}),
        "parsed_label_config": ("dict", {0: (None, None)}),
        "evaluate_predictions_automatically": None,
        "config_has_control_tags": None,
        "skip_queue": None,
        "reveal_preannotations_interactively": None,
        "pinned_at": "datetime",
        "finished_task_number": "integer",
        "queue_total": "integer",
        "queue_done": "integer",
    }
    response = client.projects.get(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.projects.get(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert (
        client.projects.delete(id=1)  # type: ignore[func-returns-value]
        is None
    )

    assert (
        await async_client.projects.delete(id=1)  # type: ignore[func-returns-value]
        is None
    )


async def test_update(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "title": "My project",
        "description": "My first project",
        "label_config": "<View>[...]</View>",
        "expert_instruction": "Label all cats",
        "show_instruction": True,
        "show_skip_button": True,
        "enable_empty_annotation": True,
        "show_annotation_history": True,
        "reveal_preannotations_interactively": True,
        "show_collab_predictions": True,
        "maximum_annotations": 1,
        "annotation_limit_count": 1,
        "annotation_limit_percent": 1.1,
        "color": "color",
        "control_weights": {
            "my_bbox": {"type": "RectangleLabels", "labels": {"Car": 1, "Airplaine": 0.5}, "overall": 0.33}
        },
    }
    expected_types: typing.Any = {
        "title": None,
        "description": None,
        "label_config": None,
        "expert_instruction": None,
        "show_instruction": None,
        "show_skip_button": None,
        "enable_empty_annotation": None,
        "show_annotation_history": None,
        "reveal_preannotations_interactively": None,
        "show_collab_predictions": None,
        "maximum_annotations": "integer",
        "annotation_limit_count": "integer",
        "annotation_limit_percent": None,
        "color": None,
        "control_weights": ("dict", {0: (None, None)}),
    }
    response = client.projects.update(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.projects.update(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_import_tasks(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "task_count": 1,
        "annotation_count": 1,
        "predictions_count": 1,
        "duration": 1.1,
        "file_upload_ids": [1],
        "could_be_tasks_list": True,
        "found_formats": ["found_formats"],
        "data_columns": ["data_columns"],
    }
    expected_types: typing.Any = {
        "task_count": "integer",
        "annotation_count": "integer",
        "predictions_count": "integer",
        "duration": None,
        "file_upload_ids": ("list", {0: "integer"}),
        "could_be_tasks_list": None,
        "found_formats": ("list", {0: None}),
        "data_columns": ("list", {0: None}),
    }
    response = client.projects.import_tasks(id=1, request=[{"key": "value"}])
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.projects.import_tasks(id=1, request=[{"key": "value"}])
    validate_response(async_response, expected_response, expected_types)


async def test_validate_config(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {"label_config": "label_config"}
    expected_types: typing.Any = {"label_config": None}
    response = client.projects.validate_config(id=1, label_config="label_config")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.projects.validate_config(id=1, label_config="label_config")
    validate_response(async_response, expected_response, expected_types)
