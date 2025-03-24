from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Admin, Book
from .serializers import AdminSerializer, BookSerializer

def home(request):
    return render(request, 'home.html')

# Admin Signup (API)
class AdminSignup(APIView):
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Admin Login (API)
class AdminLogin(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            admin = Admin.objects.get(email=email, password=password)
            serializer = AdminSerializer(admin)
            return Response(serializer.data)
        except Admin.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_404_NOT_FOUND)

# Book CRUD Operations (API)
class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None

    def get(self, request, pk):
        book = self.get_object(pk)
        if book:
            serializer = BookSerializer(book)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        book = self.get_object(pk)
        if book:
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        book = self.get_object(pk)
        if book:
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

# HTML Views
def book_list_html(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail_html(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def book_create_html(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        published_date = request.POST.get('published_date')
        Book.objects.create(title=title, author=author, isbn=isbn, published_date=published_date)
        return redirect('book-list-html')
    return render(request, 'book_create.html')

def book_update_html(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.isbn = request.POST.get('isbn')
        book.published_date = request.POST.get('published_date')
        book.save()
        return redirect('book-list-html')
    return render(request, 'book_update.html', {'book': book})

def book_delete_html(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list-html')
    return render(request, 'book_delete.html', {'book': book})

def admin_signup_html(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        Admin.objects.create(name=name, email=email, password=password)
        return redirect('admin-login-html')
    return render(request, 'admin_signup.html')

def admin_login_html(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            admin = Admin.objects.get(email=email, password=password)
            return redirect('book-list-html')
        except Admin.DoesNotExist:
            return render(request, 'admin_login.html', {'error': 'Invalid credentials'})
    return render(request, 'admin_login.html')
   