from rest_framework.serializers import (                                        HyperlinkedIdentityField,                                        ModelSerializer,                                        SerializerMethodField                                        )from posts.models   import Postfrom comments.models import Commentfrom comments.api.serializers import CommentSerializerfrom accounts.api.serializers import UserDetailSerializerclass PostCreateUpdateSerializer(ModelSerializer):    class Meta:        model = Post        fields =[            'title',            'content',            'publish',        ]post_detail_url = HyperlinkedIdentityField(                                            view_name='posts-api:api_detail',                                            lookup_field='slug'                                        )class PostDetailSerializer(ModelSerializer):    url=post_detail_url    # user = SerializerMethodField()    user = UserDetailSerializer(read_only=True)    image = SerializerMethodField()    html = SerializerMethodField()    comments = SerializerMethodField()    class Meta:        model = Post        fields =[            'id',            'url',            'title',            'user',            'slug',            'content',            'html',            'publish',            'image',            'comments',        ]    def get_html(self,obj):        return obj.get_markdown()    # def get_user(self,obj):    #     return str(obj.user.username)    def get_image(self,obj):        try:            image = obj.image.url        except:            image = None        return image    def get_comments(self,obj):        c_qs = Comment.objects.filter_by_instance(obj)        comments = CommentSerializer(c_qs,many=True).data        return commentsclass PostListSerializer(ModelSerializer):    url = post_detail_url    # delete_url = HyperlinkedIdentityField(    #                     view_name='posts-api:api_delete',    #                     lookup_field='slug'    #                 )    # user = SerializerMethodField()    user = UserDetailSerializer(read_only=True)    class Meta:        model = Post        fields = [            'url',            'title',            'user',            'content',            'publish',            # 'delete_url'        ]    # def get_user(self,obj):    #     return str(obj.user.username)"""        data ={"title":"title 1","content":"new cnrtent","publish":"2020-11-11","slug":"new-slug"}new_item = PostSerializer(data = data)if new_item.is_valid():    new_item.save()else:    print(new_item.errors)      from posts.models import Postfrom posts.api.serializers import PostDetailSerializerdata ={"title":"title 1","content":"new cnrtent","publish":"2020-11-11","slug":"new-slug-new"}    obj = Post.objects.get(id=2)new_item = PostDetailSerializer(obj,data = data)if new_item.is_valid():    new_item.save()else:    print(new_item.errors)                      """