        // adding limit to package names inside individual package
        let tourInfo = document.body.querySelectorAll('.tour-info')
        let packageName = document.body.querySelectorAll('.package-name')
        for(let i=0;i < tourInfo.length;i++){
            tour = tourInfo[i]
            pack = tour.querySelectorAll('.package-name')
            if(pack.length > 10){
                for(let j=pack.length; j > 10; j--){
                    pack[j-1].classList.add('hidden')
                }
            }
        }

        // adding reverse field on homepage
        let ventureInfo = document.body.querySelectorAll('.venture-info')
        for(let i=1;i<=ventureInfo.length - 1; i += 2){
            ventureInfo[i].classList.add('reverse')
        }

        // setting rows length in tours.html to 3 for now
        const tableBody = document.querySelectorAll('.table-body')
        tableBody.forEach(function(table){
            let tableRow = table.querySelectorAll('#table-row');
            if(tableRow.length >= 11){
                for (let k=tableRow.length - 1; k > 9;k--){
                    const specificRow = tableRow[k]
                    table.removeChild(specificRow)
                }
            }
        })

        // collapsing navbar

        const navBarCollapse = document.getElementById('navbarSupportedContent');
        console.log(navBarCollapse)
        const navBtn = document.body.querySelector('.navbar-toggler');
        console.log(navBtn)
        navBtn.addEventListener('click', function(){
            const hide = navBarCollapse.classList.contains('show');
            console.log(hide)
            if (hide) {
                navBarCollapse.classList.remove('show', 'collapse')
            }
        })