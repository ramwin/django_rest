#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-08-26 17:12:41


from rest_framework import permissions


class IsPostAuthor(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        print(request.method)
        return False
        return obj.user == request.user
