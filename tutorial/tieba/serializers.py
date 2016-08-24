#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-08-16 16:16:46

from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=255)
    content = serializers.CharField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
