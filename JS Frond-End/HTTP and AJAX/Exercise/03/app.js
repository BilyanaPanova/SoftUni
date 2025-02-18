function attachEvents() {
  const baseURL = 'http://localhost:3030/jsonstore/collections/students';

  const tableBody = document.querySelector('#results tbody');
  const submitButton = document.getElementById('submit');

  const inputs = {
      firstName: document.querySelector('input[name="firstName"]'),
      lastName: document.querySelector('input[name="lastName"]'),
      facultyNumber: document.querySelector('input[name="facultyNumber"]'),
      grade: document.querySelector('input[name="grade"]'),
  };

  window.addEventListener('load', loadStudents);
  submitButton.addEventListener('click', addStudent);

  function loadStudents() {
      tableBody.innerHTML = '';
      fetch(baseURL)
          .then(response => response.json())
          .then(data => {
              Object.values(data).forEach(student => {
                  const tr = document.createElement('tr');

                  const firstNameCell = createCell(student.firstName);
                  const lastNameCell = createCell(student.lastName);
                  const facultyNumberCell = createCell(student.facultyNumber);
                  const gradeCell = createCell(student.grade);

                  tr.appendChild(firstNameCell);
                  tr.appendChild(lastNameCell);
                  tr.appendChild(facultyNumberCell);
                  tr.appendChild(gradeCell);
                  tableBody.appendChild(tr);
              });
          })
          .catch(error => console.error('Error loading students:', error));
  }

  function addStudent() {

      const firstName = inputs.firstName.value.trim();
      const lastName = inputs.lastName.value.trim();
      const facultyNumber = inputs.facultyNumber.value.trim();
      const grade = inputs.grade.value.trim();

      if (!firstName || !lastName || !facultyNumber || !grade || isNaN(grade) || isNaN(facultyNumber)) {
          alert('All fields are required and must be valid!');
          return;
      }

      const student = {
          firstName,
          lastName,
          facultyNumber,
          grade,
      };

      fetch(baseURL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(student),
      })
          .then(response => response.json())
          .then(() => {
              inputs.firstName.value = '';
              inputs.lastName.value = '';
              inputs.facultyNumber.value = '';
              inputs.grade.value = '';
              loadStudents(); 
          })
          .catch(error => console.error('Error adding student:', error));
  }

  function createCell(content) {
      const td = document.createElement('td');
      td.textContent = content;
      return td;
  }

}

attachEvents();
