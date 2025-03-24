from django.urls import path
from .views import home, AdminSignup, AdminLogin, BookList, BookDetail, book_list_html, book_detail_html, book_create_html, book_update_html, book_delete_html, admin_signup_html, admin_login_html

urlpatterns = [
    path('', home, name='home'),
    
    # API Endpoints
    path('api/admin/signup/', AdminSignup.as_view(), name='admin-signup'),
    path('api/admin/login/', AdminLogin.as_view(), name='admin-login'),
    path('api/books/', BookList.as_view(), name='book-list'),
    path('api/books/<int:pk>/', BookDetail.as_view(), name='book-detail'),

    # HTML Endpoints
    path('html/books/', book_list_html, name='book-list-html'),
    path('html/books/<int:pk>/', book_detail_html, name='book-detail-html'),
    path('html/books/create/', book_create_html, name='book-create-html'),
    path('html/books/<int:pk>/update/', book_update_html, name='book-update-html'),
    path('html/books/<int:pk>/delete/', book_delete_html, name='book-delete-html'),
    path('html/admin/signup/', admin_signup_html, name='admin-signup-html'),
    path('html/admin/login/', admin_login_html, name='admin-login-html'),
    
]