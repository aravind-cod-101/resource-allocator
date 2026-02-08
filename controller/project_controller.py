from fastapi import Depends
from database import db_session
from repositories import project_repo
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session


class ProjectController:
    def match_resources(
        self, project_id: int, db: Session = Depends(db_session.get_db)
    ):
        results = project_repo.match_resources(project_id, db)
        if not results:
            return JSONResponse(
                status_code=404, content={"status": False, "message": "No tasks found"}
            )

        return {"status": True, "data": results}


project_controller = ProjectController()
