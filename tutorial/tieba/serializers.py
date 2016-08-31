#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-08-16 16:16:46

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Test
from .models import Album, Track


class PostSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=255)
    content = serializers.CharField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)


class TestSerializer(serializers.ModelSerializer):
    text = serializers.ReadOnlyField()
    pass

    class Meta:
        model = Test
        excludes = ()


class UserSerializer2(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False, max_length=255)


class UserSerializer(serializers.ModelSerializer):
    # test = serializers.ReadOnlyField(source='test')
    class Meta:
        model = User
        fields = ('username','id',)


class AlbumSerializer(serializers.ModelSerializer):
    # tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')
