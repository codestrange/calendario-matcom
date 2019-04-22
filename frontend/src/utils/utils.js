export const convertGroupsToStr = function (groups) {
    let result = '';
    for (let i = 0; i < groups.length; ++i)
        result += groups[i].name + ((i + 1 !== groups.length) ? ', ' : ' ');
    return result;
};