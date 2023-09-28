from marshmallow import Schema, fields

class LevelSchema(Schema):
  id = fields.Str(dump_only = True)
  body = fields.Str(required = True)
  student_id = fields.Int(required = True)
  timestamp = fields.Str(dump_only=True)

class StudentSchema(Schema):
  id = fields.Str(dump_only = True)
  username = fields.Str(required = True)
  email = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True)
  first_name = fields.Str()
  last_name = fields.Str()
  
class StudentSchemaNested(StudentSchema):
  levels = fields.List(fields.Nested(LevelSchema), dump_only=True)
  followed = fields.List(fields.Nested(StudentSchema), dump_only=True)

class UpdateStudentSchema(Schema):
  username = fields.Str()
  email = fields.Str()
  password = fields.Str(required = True, load_only = True)
  new_password = fields.Str()
  first_name = fields.Str()
  last_name = fields.Str()

class DeleteStudentSchema(Schema):
  username = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True)