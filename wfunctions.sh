#!/usr/bin/env bash
se () {    history | rg -i $1 }
manv () { man $1 | v -c 'set nonumber' - }
#wi () { whereis $1}
ex () { exiftool -j $1 | v - }
lcd () { 
  echo  ${FUNCNAME[0]}
  ls -d */
}
take () { mkdir -p -- "$1" && cd -P -- "$1"; } 
rgg () { rg $1 /mnt/c/all/gcloud_his $HISTFILE }

cha() {
   fd -H -I --changed-within $1mins | rg -v '\.git' | rg -v '\theia'
}
hit() { history | tail -n $1 }

#https://raw.githubusercontent.com/nickjj/dotfiles/master/.config/zsh/.aliases
vdiff () {
    if [ "${#}" -ne 2 ] ; then

        printf "vdiff requires two arguments"
        echo "  comparing dirs:  vdiff dir_a dir_b"
        echo "  comparing files: vdiff file_a file_b"
        return 1
    fi

    local left="${1}"
    local right="${2}"

    if [ -d "${left}" ] && [ -d "${right}" ]; then
        nvim +"DirDiff ${left} ${right}"
    else
        nvim -d "${left}" "${right}"
    fi
}
