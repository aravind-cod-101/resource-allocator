
from sqlalchemy.orm import Session
from models import Task, Skill, Resource, ResourceAvailability, ResourceSkill, Project
from config import logger


class ProjectRepo:
    def get_tasks(self, project_id: int, db: Session):
        return (
            db.query(
            Task.id,
            Task.name,
            Task.start_date,
            Task.end_date,
            Project.name.label("project_name"),
            Skill.name.label("skill_name"),
            Project.id.label("project_id"),
            Skill.id.label("skill_id") 
                ) 
                .join(Project, Project.id == Task.project_id)
                .join(Skill, Skill.id == Task.skill_id)
                .filter(Task.project_id == project_id)
                .all()
        )
        
    def get_resources(self, task, db: Session):
        return (
                db.query(
                    Resource.id,
                    Resource.name
                    )
                .join(ResourceSkill, ResourceSkill.resource_id == Resource.id)
                .join(ResourceAvailability, ResourceAvailability.resource_id == Resource.id)
                .filter(ResourceSkill.skill_id == task.skill_id)
                .filter(ResourceAvailability.available_from <= task.start_date)
                .filter(ResourceAvailability.available_to >= task.end_date)
                .all()
            )
    
    def match_resources(self, project_id: int, db: Session):
        tasks = self.get_tasks(project_id, db)
                    
        logger.info(f"Found {len(tasks)} tasks for project_id - {project_id}")
        
        results = []
        for task in tasks:
            resources = self.get_resources(task, db)
            
            logger.info(f"Found {len(resources)} resources for task - {task.name}")

            results.append({
                "task" : {
                    "id" : task.id,
                    "project_name": task.project_name,
                    "task_name": task.name,
                    "skill": task.skill_name,
                    "start_date": task.start_date.isoformat(),
                    "end_date": task.end_date.isoformat(),
                    },
                "resources": [{"id": r.id, "name": r.name } for r in resources]
            })               
        
        return results
       
project_repo = ProjectRepo()