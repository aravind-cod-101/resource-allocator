from fastapi import APIRouter, Depends
from controller import project_controller
from middlewares import verify_api_key

router = APIRouter(dependencies=[Depends(verify_api_key)])

router.get('/{project_id}/resources')(project_controller.match_resources)