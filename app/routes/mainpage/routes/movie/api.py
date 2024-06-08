from fastapi import APIRouter, HTTPException

from .fuc import sf_fantasy, liberal_others, family, drama, romance, action, animations

router = APIRouter(prefix='/movie')

@router.get('/SF-fantasy')
async def magepage_SF_fantasy_list():
    try:
        data = await sf_fantasy()
        return data

    except:
        raise HTTPException(status_code=400, detail='error')

@router.get('/Liberal-Arts-Others')
async def magepage_Liberal_Others_list():
    try:
        data = await liberal_others()
        return data
    except: 
        raise HTTPException(status_code=400, detail='error')
    
@router.get('/family')
async def magepage_family_list():
    try:
        data = await family()
        return data
    except: 
        raise HTTPException(status_code=400, detail='error')
    
@router.get('/drama')
async def magepage_drama_list():
    try:
        data = await drama()
        return data
    except: 
        raise HTTPException(status_code=400, detail='error')
    
@router.get('/romance')
async def magepage_romance_list(user_id: int):
    try:
        data = await romance()
        return data
    except: 
        raise HTTPException(status_code=400, detail='error')

@router.get('/action')
async def magepage_action_list():
    try:
        data = await action()
        return data
    except: 
        raise HTTPException(status_code=400, detail='error')
    
@router.get('/animations')
async def magepage_watch_list():
    try:
        data = await animations()
        return data
    except: 
        raise HTTPException(status_code=400, detail='error')