<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <!-- <meta name="generator" content="Astro v5.9.2"> -->
    <?php
        // require('sign-in.php');
        require('css.php');
        require('../../includes/main.php');
        echo title('Signin | Futsuga');
    ?>
    <link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/sign-in/">
    <script src="../../assets/js/color-modes.js"></script>
    <link href="../../assets/dist/css/bootstrap.min.css" rel="stylesheet">
    <meta name="theme-color" content="#712cf9">
    <!-- <link href="sign-in.css" rel="stylesheet"> -->
</head>

<body class="d-flex align-items-center py-4 bg-body-tertiary">
    <!--?php 
        require('../../includes/menu.php');
        // pages($now='');
        echo '<br><br><br><br><br><br><br><br><br><br><br><br><br>';
    ?-->
    <div class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle"> <button
            class="btn btn-bd-primary py-2 dropdown-toggle d-flex align-items-center" id="bd-theme" type="button"
            aria-expanded="false" data-bs-toggle="dropdown" aria-label="Toggle theme (auto)"> <svg
                class="bi my-1 theme-icon-active" aria-hidden="true">
                <use href="#circle-half"></use>
            </svg> <span class="visually-hidden" id="bd-theme-text">Toggle theme</span> </button>
        <ul class="dropdown-menu dropdown-menu-end shadow" aria-labelledby="bd-theme-text">
            <li> <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="light"
                    aria-pressed="false"> <svg class="bi me-2 opacity-50" aria-hidden="true">
                        <use href="#sun-fill"></use>
                    </svg>
                    Light
                    <svg class="bi ms-auto d-none" aria-hidden="true">
                        <use href="#check2"></use>
                    </svg> </button> </li>
            <li> <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="dark"
                    aria-pressed="false"> <svg class="bi me-2 opacity-50" aria-hidden="true">
                        <use href="#moon-stars-fill"></use>
                    </svg>
                    Dark
                    <svg class="bi ms-auto d-none" aria-hidden="true">
                        <use href="#check2"></use>
                    </svg> </button> </li>
            <li> <button type="button" class="dropdown-item d-flex align-items-center active" data-bs-theme-value="auto"
                    aria-pressed="true"> <svg class="bi me-2 opacity-50" aria-hidden="true">
                        <use href="#circle-half"></use>
                    </svg>
                    Auto
                    <svg class="bi ms-auto d-none" aria-hidden="true">
                        <use href="#check2"></use>
                    </svg> </button> </li>
        </ul>
    </div>
    <main class="form-signin w-100 m-auto">
        <form method="post" action="/pages/auth/sign-in.php" address="/auth/sign-in.php"> <!--img class="mb-4" src="../assets/brand/bootstrap-logo.svg" alt="" width="72" height="57"-->
            <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
            <div class="form-floating"> <input name='email' type="email" class="form-control" id="floatingInput"
                    placeholder="name@example.com"> <label for="floatingInput">Email address</label>
            </div>
            <div class="form-floating"> <input name="password" type="password" class="form-control" id="floatingPassword"
                    placeholder="Password"> <label for="floatingPassword">Password</label>
            </div>
            <button class="btn btn-primary w-100 py-2" type="submit">Sign in</button>
            <p class="mt-5 mb-3 text-body-secondary">&copy; <?= date('Y') ?></p>
        </form>
    </main>
    <script src="../assets/dist/js/bootstrap.bundle.min.js" class="astro-vvvwv3sm"></script>
</body>
</html>