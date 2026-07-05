from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    test_email = "tester@mergington.edu"
    activity = activities[activity_name]

    if test_email not in activity["participants"]:
        activity["participants"].append(test_email)

    response = client.delete(f"/activities/{activity_name}/participants/{test_email}")

    assert response.status_code == 200
    assert test_email not in activity["participants"]
    assert response.json()["message"] == f"Unregistered {test_email} from {activity_name}"
