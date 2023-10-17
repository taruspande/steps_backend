from django.db import models

class Scanner(models.Model):
    gate_number = models.CharField(max_length=20, unique=True)
    scanner_number = models.PositiveIntegerField(unique=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    encrypted_code = models.CharField(max_length=100)  # Store the encrypted code for the event
    def __str__(self):
        return f"Scanner {self.scanner_number} at Gate {self.gate_number}"

class Entry(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  
    gate_number = models.CharField(max_length=20)
    scanner = models.ForeignKey(Scanner, on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entry for {self.user} at Gate {self.gate_number}"
