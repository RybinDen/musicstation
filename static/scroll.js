var scroller = document.querySelector("#scroller");
var loaded = document.querySelector("#loaded");
var sentinel = document.querySelector('#sentinel');
var counter = 20;
function loadItems() {
  fetch(`/radio/load?c=${counter}`).then((response) => {
    response.json().then((response) => {
      if (!response.length) {
        sentinel.innerHTML = "No more posts";
        return;
      }

//console.log(response);
$.each(response, function(index, value) {
  $("#list-radio").append("<div class=\"radio\" data-id=\"" + value.stationuuid + "\">" + value.name + "</div>");
});
// обновляем инфу на странице
counter = document.getElementsByClassName('radio').length; //response.length; // переделать, подсчитывать не в response а общее число станций на странице
loaded.innerText = `${counter} items loaded`;
console.log(counter);

    })
  })
}

// Create a new IntersectionObserver instance
var intersectionObserver = new IntersectionObserver(entries => {
  // Uncomment below to see the entry.intersectionRatio when
  // the sentinel comes into view
  // entries.forEach(entry => {
  //   console.log(entry.intersectionRatio);
  // })
  // If intersectionRatio is 0, the sentinel is out of view
  // and we don't need to do anything. Exit the function
  if (entries[0].intersectionRatio <= 0) {
    return;
  }
  // Call the loadItems function
  loadItems();
});
// Instruct the IntersectionObserver to watch the sentinel
intersectionObserver.observe(sentinel);
