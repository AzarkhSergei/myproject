document.getElementById("companyStatus").onclick = myCompanyStatus;

function myCompanyStatus() {
  fetch('/employees')
    .then(response => response.json())
    .then(data => {
      const status = document.getElementById("status");
      status.innerHTML = "<h2>My Company:</h2>";
      const statusList = document.getElementById("employeesList");
      // Очищаем список сотрудников перед добавлением новых данных
      statusList.innerHTML = "";
      data.forEach(e => {
        const li = createElement(`ID: ${e.id}, First name: ${e.firstName}, Last name: ${e.lastName}, Birth Date: ${e.birthDate}, Salary: ${e.salary} NIS`, "li");
        statusList.appendChild(li);
      });
    })
    .catch(error => console.error('Error fetching employee data:', error));
}

function createElement(text, tag) {
  const element = document.createElement(tag);
  const textElement = document.createTextNode(text);
  element.append(textElement);
  return element;
}
