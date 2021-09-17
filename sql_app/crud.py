from sqlalchemy.orm import Session, session
from typing import List

from . import models, schemas

# App Name
def get_app_name_all(db: Session):
    return db.query(models.AppName).all()

def get_app_name(db: Session, id_app: int):
    return db.query(models.AppName).filter(models.AppName.id_app == id_app).first()

def get_app_name_by_name(db: Session, app_name: str):
    return db.query(models.AppName).filter(models.AppName.app_name == app_name).first()

def create_app_name(db: Session, data: schemas.AppNameCreate):
    new = models.AppName(
        app_name = data.app_name
    )
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

# Current Version
def get_current_version_all(db: Session):
    return db.query(models.CurrentVersion).filter(
        models.CurrentVersion.id_flag == 1
    ).all()

def get_current_version(db: Session, id_app: int):
    return db.query(models.CurrentVersion).filter(
        models.CurrentVersion.id_app == id_app,
        models.CurrentVersion.id_flag == 1
        ).all()

def create_current_versions(db: Session, data: List[schemas.CurrentVersionCreate], length: int):
    for index in range(length):
        new = models.CurrentVersion(
            id_app = data[index].id_app,
            current_version = data[index].current_version,
            keterangan = data[index].keterangan,
            id_flag = 1
        )
        db.add(new)
        db.commit()
        db.refresh(new)
    return new

def create_current_version(db: Session, data: List[schemas.CurrentVersionCreate], index: int):
    new = models.CurrentVersion(
        id_app = data[index].id_app,
        current_version = data[index].current_version,
        keterangan = data[index].keterangan,
        id_flag = 1
    )
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

# CVE App
def get_cve_all(db: Session):
    return db.query(models.Cve).filter(
        models.Cve.id_flag == 1
    ).all()

def get_cve(db: Session, id_app: int):
    return db.query(models.Cve).filter(
        models.Cve.id_app == id_app,
        models.Cve.id_flag == 1
        ).first()

def create_cve(db: Session, data: schemas.CveCreate):
    new = models.Cve(
        id_app = data.id_app,
        cve = data.cve,
        cve_link = data.cve_link,
        id_flag = 1
    )
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

# Latest Version
def get_latest_version_all(db: Session):
    return db.query(models.LatestVersion).filter(
        models.LatestVersion.id_flag == 1
    ).all()

def get_latest_version(db: Session, id_app: int):
    return db.query(models.LatestVersion).filter(
        models.LatestVersion.id_app == id_app,
        models.LatestVersion.id_flag == 1
        ).first()

def create_latest_version(db: Session, data: schemas.LatestVersionCreate):
    new = models.LatestVersion(
        id_app = data.id_app,
        latest_version = data.latest_version,
        release_notes = data.release_notes,
        id_flag = 1
    )
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

# Status App
def get_status_all(db: Session):
    return db.query(models.StatusApp).filter(
        models.StatusApp.id_flag == 1
    ).all()

def get_status(db: Session, id_app: int):
    return db.query(models.StatusApp).filter(
        models.StatusApp.id_app == id_app,
        models.StatusApp.id_flag == 1
        ).first()

def create_status(db: Session, data: schemas.StatusAppCreate):
    new = models.StatusApp(
        id_app = data.id_app,
        status = data.status,
        id_flag = 1
    )
    db.add(new)
    db.commit()
    db.refresh(new)
    return new