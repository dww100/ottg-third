console.log("Starting Spec.js");

describe("Superlists Javascript", () =>  {
  const inputId = "id_text";
  const errorClass = "invalid-feedback";
  const inputSelector = `#${inputId}`;
  const errorSelector = `.${errorClass}`;
  let testDiv;
  let textInput;
  let errorMsg;

  beforeEach(() => {
    console.log("beforeEach");
    testDiv = document.createElement('div');
    testDiv.innerHTML = `
      <form>
        <input  
          id="${inputId}"
          name="text"
          class="form-control form-control-lg is-invalid"
          placeholder="Enter a to-do item"
          value="Value as submitted"
          aria-describedby="id_text_feedback"
          required
        />
        <div id="id_text_feedback" class="${errorClass}">An error message</div>
      </form>
    `;
    document.body.appendChild(testDiv);
    textInput = document.querySelector(inputSelector);
    errorMsg = document.querySelector(errorSelector);
  });

  afterEach(() => {
    testDiv.remove();
  });

  it("should have a useful html fixture", () => {
    console.log("Running HTML fixture test");
    expect(errorMsg.checkVisibility()).toBeTrue();
  });

  it("should hide error message on input", () => {
    console.log("Running hide error message test");
    initialize(inputSelector);
    textInput.dispatchEvent(new Event('input'));
    expect(errorMsg.checkVisibility()).toBeFalse();
  });

  it("should not hide error message before input", () => {
    console.log("Running no hide before input test");
    initialize(inputSelector);
    expect(errorMsg.checkVisibility()).toBeTrue();
  });


});