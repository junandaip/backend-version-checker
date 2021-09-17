from typing import List

from fastapi import Depends, FastAPI, HTTPException, status, Response
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import exists, table

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -----------------------------GET DATA-----------------------------
@app.get("/all/{id_app}")
def get_all_data(id_app: int, db: Session = Depends(get_db)):
    app_name = get_one_app_name(id_app, db)
    # current_ver = get_specific_current_version(id_app, db)
    latest_ver = get_one_latest_version(id_app, db)
    cve = get_one_cve(id_app, db)
    app_status = get_one_status(id_app, db)
    return[app_name, latest_ver, cve, app_status]

# -----------------------------APP NAME-----------------------------
@app.get("/app-names/", response_model=List[schemas.AppName])
def get_all_app_names(db: Session = Depends(get_db)):
    get = crud.get_app_name_all(db)
    return get

@app.get("/app-name/{id_app}", response_model=schemas.AppName)
def get_one_app_name(id_app: int, db: Session = Depends(get_db)):
    get = crud.get_app_name(db, id_app=id_app)
    if get is None:
        raise HTTPException(status_code=404, detail="Application not found")
    return get

@app.post("/app-name/", response_model=schemas.AppName, status_code=status.HTTP_201_CREATED)
def create_new_app_name(app: schemas.AppNameCreate, db: Session = Depends(get_db)):
    get = crud.get_app_name_by_name(db, app_name=app.app_name)
    if get:
        raise HTTPException(status_code=400, detail="Application already exists")
    return crud.create_app_name(db=db, data=app)

# -----------------------------CURRENT VERSION-----------------------------
@app.get("/current-versions/", response_model=List[schemas.CurrentVersion])
def get_all_current_versions(db: Session = Depends(get_db)):
    get = crud.get_current_version_all(db)
    return get

@app.get("/current-version/{id_app}", response_model=List[schemas.CurrentVersion])
def get_specific_current_version(id_app: int, db: Session = Depends(get_db)):
    get = crud.get_current_version(db, id_app=id_app)
    if get is None:
        print("current version kosong")
        # raise HTTPException(status_code=404, detail="Data not found")
    return get

@app.post("/current-version/", status_code=status.HTTP_201_CREATED)
def create_new_current_version(data: List[schemas.CurrentVersionCreate], db: Session = Depends(get_db)):
    exists = db.query(models.CurrentVersion).first()
    if exists is not None:
        curr_ver = db.query(models.CurrentVersion).filter(
            models.CurrentVersion.id_flag == 1
        ).all()
        for i in curr_ver:
            i.id_flag=2
        crud.create_current_versions(db=db, data=data, length=len(data))
    else:
        crud.create_current_versions(db=db, data=data, length=len(data))
    return data

# Check one by one 
    # for idx, i in enumerate(data):
    #     exists = db.query(models.CurrentVersion).filter(
    #         models.CurrentVersion.id_app == i.id_app
    #     ).all()

    #     if len(exists) > 0:
    #         for x in exists:
    #             if i.current_version == x.current_version and i.keterangan == x.keterangan:
    #                 print("data sudah ada")
    #             else:
                      # Needs logic here to check current_ver and keterangan to match
    #                 x.id_flag=2
    #                 crud.create_current_version(db=db, data=data, index=idx)
    #     else:
    #         # print("empty")
    #         crud.create_current_version(db=db, data=data, index=idx)                           

 # -----------------------------CVE APP-----------------------------
@app.get("/cves/", response_model=List[schemas.Cve])
def get_all_cves(db: Session = Depends(get_db)):
    get = crud.get_cve_all(db)
    return get

@app.get("/cve/{id_app}", response_model=schemas.Cve)
def get_one_cve(id_app: int, db: Session = Depends(get_db)):
    get = crud.get_cve(db, id_app=id_app)
    if get is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return get

@app.post("/cve/", response_model=schemas.Cve, status_code=status.HTTP_201_CREATED)
def create_new_cve(data: schemas.CveCreate, db: Session = Depends(get_db)):

    exists = db.query(models.Cve).filter(
        models.Cve.id_app == data.id_app,
        models.Cve.id_flag == 1
        ).first()

    if exists is not None:
        if (exists.cve == data.cve and
            exists.cve_link == data.cve_link):
            raise HTTPException(status_code=400, detail="data already exists")
        else:
            exists.id_flag = 2
            return crud.create_cve(db=db, data=data)
    else:
        return crud.create_cve(db=db, data=data)

# -----------------------------LATEST VERSION-----------------------------
@app.get("/latest-versions/", response_model=List[schemas.LatestVersion])
def get_all_latest_versions(db: Session = Depends(get_db)):
    get = crud.get_latest_version_all(db)
    return get

@app.get("/latest-version/{id_app}", response_model=schemas.LatestVersion)
def get_one_latest_version(id_app: int, db: Session = Depends(get_db)):
    get = crud.get_latest_version(db, id_app=id_app)
    if get is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return get

@app.post("/latest-version/", response_model=schemas.LatestVersion, status_code=status.HTTP_201_CREATED)
def create_new_latest_version(data: schemas.LatestVersionCreate, db: Session = Depends(get_db)):

    exists = db.query(models.LatestVersion).filter(
        models.LatestVersion.id_app == data.id_app,
        models.LatestVersion.id_flag == 1
        ).first()

    if exists is not None:
        if (exists.latest_version == data.latest_version and
            exists.release_notes == data.release_notes):
            raise HTTPException(status_code=400, detail="data already exists")
        else:
            exists.id_flag = 2
            return crud.create_latest_version(db=db, data=data)
    else:
        return crud.create_latest_version(db=db, data=data)

# -----------------------------STATUS APP-----------------------------
@app.get("/status-all/", response_model=List[schemas.StatusApp])
def get_all_status(db: Session = Depends(get_db)):
    get = crud.get_status_all(db)
    return get

@app.get("/status/{id_app}", response_model=schemas.StatusApp)
def get_one_status(id_app: int, db: Session = Depends(get_db)):
    get = crud.get_status(db, id_app=id_app)
    if get is None:
        print("Application's status is empty")
        # raise HTTPException(status_code=404, detail="Application's Status not found")
    return get

@app.post("/status/", response_model=schemas.StatusApp, status_code=status.HTTP_201_CREATED)
def create_new_status(data: schemas.StatusAppCreate, db: Session = Depends(get_db)):

    exists = db.query(models.StatusApp).filter(
        models.StatusApp.id_app == data.id_app,
        models.StatusApp.id_flag == 1
        ).first()

    if exists is not None:
        if  exists.status == data.status:
            raise HTTPException(status_code=400, detail="data already exists")
        else:
            exists.id_flag = 2
            return crud.create_status(db=db, data=data)
    else:
        return crud.create_status(db=db, data=data)