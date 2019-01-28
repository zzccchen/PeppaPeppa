let util = {

};
util.title = function (title) {
    title = title ? title + ' - Home' : 'PeppaPeppa';
    window.document.title = title;
};

export default util;