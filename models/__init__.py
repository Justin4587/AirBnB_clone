#!/usr/bin/python3
import models.engine.file_storage
import models.base_model
master_dict = {"BaseModel": base_model.BaseModel}
storage = models.engine.file_storage.FileStorage()
storage.reload()
