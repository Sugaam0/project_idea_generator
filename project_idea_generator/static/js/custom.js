
  // Function to dismiss a specific message
  function dismissMessage(element) {
    const alert = element.parentElement;
    alert.style.opacity = '0';
    alert.style.transform = 'translateY(20px)';
    setTimeout(() => alert.remove(), 300); // Remove after fade-out
  }

  // Auto-dismiss all messages after 5 seconds
  document.addEventListener('DOMContentLoaded', function () {
    const alerts = document.querySelectorAll('.pspark-alert');
    alerts.forEach(alert => {
      setTimeout(() => {
        alert.style.opacity = '0';
        alert.style.transform = 'translateY(20px)';
        setTimeout(() => alert.remove(), 300); // Remove after fade-out
      }, 5000); // Dismiss after 5 seconds
    });
  });
