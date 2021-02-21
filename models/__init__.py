#!/usr/bin/python3
import models.engine.file_storage
import models.base_model
import models.user
master_dict = {"BaseModel": base_model.BaseModel,
                "User": user.User}
storage = models.engine.file_storage.FileStorage()
storage.reload()
