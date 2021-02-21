#!/usr/bin/python3
import models.engine.file_storage
import models.base_model
import models.user
import models.state
import models.amenity
import models.city
import models.review
import models.place


master_dict = {"BaseModel": base_model.BaseModel,
               "User": user.User, "State": state.State,
               "Amenity": amenity.Amenity, "City": city.City,
               "Review": review.Review, "Place": place.Place}
storage = models.engine.file_storage.FileStorage()
storage.reload()
