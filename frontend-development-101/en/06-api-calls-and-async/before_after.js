fetch(url, (res) => {
  parse(res, (data) => {
    render(data, (e) => { ... });
  });
});
