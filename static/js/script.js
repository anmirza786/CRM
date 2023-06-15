var swiper = new Swiper(".swiper", {
  loop: true,
  spaceBetween: 30,
  centeredSlides: true,
  autoplay: {
    delay: 3500,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
  },
});

const els = (sel, par) => (par || document).querySelectorAll(sel);
const otpForm = document.getElementById("otpForm");
const code = document.getElementById("code");
otpForm.addEventListener("submit", function (event) {
  event.preventDefault();
  let otpValue = "";

  const elsInput = [...els(".userInput input")];
  otpValue = elsInput.reduce((acc, input) => acc + input.value, "");
  code.value = otpValue;
  document.getElementById("otpForm").submit();
});

els(".pin").forEach((elGroup) => {
  const elsInput = [...elGroup.children];
  const len = elsInput.length;

  const handlePaste = (ev) => {
    const clip = ev.clipboardData.getData("text");
    const pin = clip.replace(/\s/g, "");
    const ch = [...pin];
    elsInput.forEach((el, i) => (el.value = ch[i] ?? ""));
    elsInput[pin.length - 1].focus();
  };

  const handleInput = (ev) => {
    const elInp = ev.currentTarget;
    const i = elsInput.indexOf(elInp);
    if (elInp.value && (i + 1) % len) elsInput[i + 1].focus();
  };

  const handleKeyDn = (ev) => {
    const elInp = ev.currentTarget;
    const i = elsInput.indexOf(elInp);
    if (!elInp.value && ev.key === "Backspace" && i) elsInput[i - 1].focus();
  };

  elsInput.forEach((elInp) => {
    elInp.addEventListener("paste", handlePaste);
    elInp.addEventListener("input", handleInput);
    elInp.addEventListener("keydown", handleKeyDn);
  });
});
// function submitForm(event) {
//   event.preventDefault();
//   let otpValue = "";

//   const elsInput = [...els(".userInput input")];
//   otpValue = elsInput.reduce((acc, input) => acc + input.value, "");
//   code.value = otpValue;
//   document.getElementById("otpForm").submit();
// }
