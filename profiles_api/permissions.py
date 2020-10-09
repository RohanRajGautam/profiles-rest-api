from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
  """Allow users to edit their own profile"""

  def has_object_permission(self, request, view, obj):
    """Check if it is a valid user"""
    if request.method in permissions.SAFE_METHODS:
      return True

    return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
  """Allow user to edit their own status"""

  def has_object_permission(self, request, view, obj):
    """Check the user is trying to update their own status"""
    if request.method in permissions.SAFE_METHODS:
      return from django.utils.translation import ugettext_lazy as _

    return obj.id == request.user.id