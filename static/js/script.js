// Budget Buddy - Main JavaScript File

// Auto-hide alerts after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });
});

// Form validation
function validateTransactionForm() {
    const amount = document.getElementById('amount').value;
    const category = document.getElementById('category').value;
    const date = document.getElementById('date').value;
    
    if (!amount || amount <= 0) {
        alert('Please enter a valid amount');
        return false;
    }
    
    if (!category) {
        alert('Please select a category');
        return false;
    }
    
    if (!date) {
        alert('Please select a date');
        return false;
    }
    
    return true;
}

// Number formatting
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR'
    }).format(amount);
}

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Delete confirmation
function confirmDelete(message) {
    return confirm(message || 'Are you sure you want to delete this item?');
}

// Print report
function printReport() {
    window.print();
}

// Export to CSV (basic implementation)
function exportToCSV() {
    // This is a placeholder - you can implement CSV export functionality
    alert('Export feature coming soon!');
}

console.log('Budget Buddy loaded successfully!');
