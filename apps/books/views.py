from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# Temporary simple AI summary function
def generate_summary(text):
    return text[:300]  # simple preview (safe for now)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        file = self.request.FILES.get('file')

        extracted_text = ""

        # Read file content (basic version)
        if file:
            try:
                extracted_text = file.read().decode('utf-8')
            except:
                extracted_text = "Could not read file"

        summary = generate_summary(extracted_text)

        serializer.save(
            user=self.request.user,   # ✅ FIXED
            summary=summary
        )