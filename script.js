document.getElementById('bookingForm').addEventListener('submit', function (e) {
  e.preventDefault();

  // Show confirmation
  const confirmation = document.getElementById('confirmation');
  confirmation.classList.remove('hidden');

  // Optionally reset form
  this.reset();
});

