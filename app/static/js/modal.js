const closeModal = document.getElementById('close-modal');

closeModal.addEventListener('click', () => {
  document.querySelector('#modal').classList.add('hidden');
});