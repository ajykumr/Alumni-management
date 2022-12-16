function getid(id) {
    return document.getElementById(id);
}

// declaration

const select_all_checkbox = getid("select-all-checkbox");
const all_checkbox_set = document.querySelectorAll('.select_all_checkbox');

// functions
if (select_all_checkbox) { select_all_checkbox.addEventListener("click", select_all_fun) }

function select_all_fun(e) {
    const all_checkbox = document.querySelectorAll('.select_all_checkbox');
    if (e.target.checked) {
        all_checkbox.forEach((item, i) => {
            item.checked = true
        });
    } else {
        all_checkbox.forEach((item, i) => {
            item.checked = false;
        });
    }
}

const searchtable = document.getElementById('searchtable')

if (searchtable) {
    searchtable.addEventListener("keydown", filtertask)
}


function filtertask(e) {
    let text = e.target.value.toLowerCase();
    let listitems = document.querySelectorAll('.table-row-one');
    listitems.forEach((item) => {
        let gotwords = item.textContent;
        if (gotwords.toLowerCase().indexOf(text) != -1) {
            item.style.display = "table-row";
        } else {
            item.style.display = "none";
        }
    });
}


// dashboard starts
const propic_btn = document.getElementById('propic_btn');
const dropdown_menu_logout_btn = document.getElementById('dropdown-menu-logout-btn');
const dropdown_menu_close_btn = document.getElementById('dropdown-menu-close-btn');
const profile_details_dropdown = document.getElementById('profile_details_dropdown');
const module_container = document.getElementById('module_container');
const module_cancel_btn = document.getElementById('module_cancel_btn');
const module_procced_btn = document.getElementById('module_procced_btn');

if (propic_btn) {
    propic_btn.addEventListener("click", propic_btn_fun);
}
if (dropdown_menu_close_btn) {
    dropdown_menu_close_btn.addEventListener("click", dropdown_menu_close_btn_fun);
}
if (dropdown_menu_logout_btn) {
    dropdown_menu_logout_btn.addEventListener("click", module_container_fun);
}
if (module_cancel_btn) {
    module_cancel_btn.addEventListener("click", module_container_fun)
}
if (module_procced_btn) {
    module_procced_btn.addEventListener("click", module_procced_btn_fun)
}


function dropdown_menu_close_btn_fun(e) {
    e.preventDefault();
    profile_details_dropdown.classList.remove("dropdown-menu-visible");
}

function propic_btn_fun(e) {
    e.preventDefault();
    profile_details_dropdown.classList.toggle("dropdown-menu-visible");
}

function module_procced_btn_fun(e) {
    module_container_fun(e)
    window.location.href = e.target.href;
}

function module_container_fun(e) {
    e.preventDefault();
    if (profile_details_dropdown) {
        dropdown_menu_close_btn_fun(e)
    }
    module_container.classList.toggle("module_container_display");
    document.body.classList.toggle("body_overflow");
}

// dashboard starts


const snackbar_container = document.getElementById("snackbar_container");
const snackbar_text = document.getElementById("snackbar_text");

if (snackbar_container) {
    if(snackbar_text.childNodes.length){
        snackbar_container.classList.add("show");
        setTimeout(function() {
            snackbar_container.classList.remove("show");
        }, 3000);
    }
}

// bulk update fun
const updateModuleOpenBtn = document.getElementById("updateModuleOpenBtn");
const moduleTwo_cancel_btn = document.getElementById("moduleTwo_cancel_btn");


const bulk_update_module_select = document.getElementById("bulk_update_module_select");
const new_bulk_module_input = document.getElementById("new_bulk_module_input");


const bulkUpdateCategoryName = document.getElementById("bulkUpdateCategoryName");
const bulkUpdateCategoryValue = document.getElementById("bulkUpdateCategoryValue");

if (new_bulk_module_input) {
    new_bulk_module_input.addEventListener("keydown", new_bulk_module_input_fun);
    new_bulk_module_input.addEventListener("blur", new_bulk_module_input_fun);
}

if (bulk_update_module_select) {
    bulk_update_module_select.addEventListener("change", bulk_update_module_select_fun);
}

if (updateModuleOpenBtn) {
    updateModuleOpenBtn.addEventListener("click", updateModuleOpenBtn_fun);
}

if (moduleTwo_cancel_btn) {
    moduleTwo_cancel_btn.addEventListener("click", updateModuleOpenBtn_fun);
}

// value update
function new_bulk_module_input_fun(e) {
    bulkUpdateCategoryValue.disabled = false;
    bulkUpdateCategoryValue.value = e.target.value;
}
function bulk_update_module_select_fun(e) {
    bulkUpdateCategoryName.disabled = false;
    bulkUpdateCategoryName.value = e.target.value;
}
function disableupdateInputs() {
    bulkUpdateCategoryValue.disabled = true;
    bulkUpdateCategoryName.disabled = true;
}

// module 2 open
function updateModuleOpenBtn_fun(e) {
    e.preventDefault()
    module_container_two.classList.toggle("module_container_display");
    document.body.classList.toggle("body_overflow");
    if (!document.body.classList.contains("body_overflow")) {
        disableupdateInputs()
    }
}


// document.body.classList.contains("body_overflow");
