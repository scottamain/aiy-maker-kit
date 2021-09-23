# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pycoral.utils.dataset import read_label_file
from coralkit import vision
import models

detector = vision.Detector(models.OBJECT_DETECTION_MODEL)
labels = read_label_file(models.OBJECT_DETECTION_LABELS)

for frame in vision.get_frames():
    objects = detector.get_objects(frame, threshold=0.4)
    vision.draw_objects(frame, objects, labels)
