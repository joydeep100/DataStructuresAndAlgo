function reverse(str){

    if (str.length === 0)
        return ''
    // another smart way would be if(str.length <= 1) return str;
    // we did not make this === to accomodate for empty str conditions as well

    return reverse(str.slice(1)) + str[0]
}
  
console.log(reverse('awesome')) // 'emosewa'
// reverse('rithmschool') // 'loohcsmhtir'