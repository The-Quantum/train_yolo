#!/bin/bash

# zip -r obj.zip /OID/Dataset/train/Vehicle\ registration\ plate/
# zip -r test.zip /OID/Dataset/validation/Vehicle\ registration\ plate/

zip -r zipperall.zip /OID/Dataset/train/Vehicle\ registration\ plate/ -x dir/Label/**\*
zip -r zipperall.zip /OID/Dataset/train/Vehicle\ registration\ plate/ -x dir/Label/**\*