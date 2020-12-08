from  flask import Flask
from flask_restful import Resource, Api, reqparse ,abort ,marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api= Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db= SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(100), nullable=False)
    views =db.Column(db.Integer,nullable=False)
    likes =db.Column(db.Integer,nullable=False)

    def __repr__ (self):
        return f"Video(name ={name},views={views},likes={likes})"


resource_fields={

    "id":fields.Integer,
    "name":fields.String,
    "views":fields.Integer,
    "likes":fields.Integer
}



videos_put_args = reqparse.RequestParser()
videos_put_args.add_argument("name", type=str, help="Name of the Video is required", required=True)
videos_put_args.add_argument("views", type = int, help="views of the video is required",required=True)
videos_put_args.add_argument("likes", type = int , help ="likes of the videois required ",required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type =str, help="Name of the Video is required")
video_update_args.add_argument("views", type =int, help="Name of the Video is required")
video_update_args.add_argument("likes", type =int, help="Name of the Video is required")



class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(409,message="couldnt find video with that id")
        return result

    @marshal_with(resource_fields)
    def put(self,video_id):
        args = videos_put_args.parse_args()
        video = VideoModel(id=video_id, name =args["name"], views =args["views"], likes=args["likes"])
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="video id taken")
        db.session.add(video)
        db.session.commit()
        return video, 201
        
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()

        if args["name"]:
            result.name = args['name']
        if  args["views"]:
            result.views=args["views"]
        if args["likes"]:
            result.likes = args["likes"]
        db.session.commit()

        return result

    


api.add_resource(Video,'/video/<int:video_id>')

if __name__ =='__main__':
    app.run(debug=True)